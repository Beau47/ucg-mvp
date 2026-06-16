import io
import contextlib
import multiprocessing as mp
import traceback

EXEC_TIMEOUT_SEC = 5

SAFE_BUILTINS = {
    "print": print,
    "range": range,
    "len": len,
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "set": set,
    "abs": abs,
    "min": min,
    "max": max,
    "sum": sum,
    "sorted": sorted,
    "round": round,
    "True": True,
    "False": False,
    "None": None,
}


def _exec_worker(code, conn):
    try:
        namespace = {"__builtins__": SAFE_BUILTINS}
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(code, namespace, namespace)
        conn.send(("ok", buf.getvalue() or "(no output)"))
    except Exception:
        conn.send(("err", traceback.format_exc()))
    finally:
        conn.close()


def run_user_code(code):
    parent_conn, child_conn = mp.Pipe(duplex=False)
    proc = mp.Process(target=_exec_worker, args=(code, child_conn))
    proc.start()
    child_conn.close()
    proc.join(timeout=EXEC_TIMEOUT_SEC)
    if proc.is_alive():
        proc.terminate()
        proc.join()
        parent_conn.close()
        return "", f"Code execution timed out ({EXEC_TIMEOUT_SEC} seconds)"
    if parent_conn.poll():
        status, payload = parent_conn.recv()
        parent_conn.close()
        if status == "ok":
            return payload, None
        return "", payload
    parent_conn.close()
    return "", "Code execution failed unexpectedly"
