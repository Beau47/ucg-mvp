"""
utils/language.py

Language utility functions.

This module serves as the single source of truth for language-related
configuration throughout the platform.

Responsibilities
----------------
- Convert Language enums into Monaco Editor language IDs.
- Provide default file extensions.
- Determine whether code execution is supported.
- Provide human-readable language names.

Keeping this logic here prevents language-specific code from being
scattered across the project.
"""

from models.problem import Language


# ==========================================================
# Monaco Editor Language IDs
# ==========================================================

MONACO_LANGUAGE_MAP = {
    Language.PYTHON: "python",
    Language.JAVA: "java",
    Language.CPP: "cpp",
    Language.C: "c",
    Language.JAVASCRIPT: "javascript",
    Language.TYPESCRIPT: "typescript",
    Language.CSHARP: "csharp",
    Language.GO: "go",
    Language.KOTLIN: "kotlin",
    Language.SWIFT: "swift",
    Language.RUST: "rust",
}


# ==========================================================
# File Extensions
# ==========================================================

FILE_EXTENSION_MAP = {
    Language.PYTHON: ".py",
    Language.JAVA: ".java",
    Language.CPP: ".cpp",
    Language.C: ".c",
    Language.JAVASCRIPT: ".js",
    Language.TYPESCRIPT: ".ts",
    Language.CSHARP: ".cs",
    Language.GO: ".go",
    Language.KOTLIN: ".kt",
    Language.SWIFT: ".swift",
    Language.RUST: ".rs",
}


# ==========================================================
# Executable Languages
# ==========================================================

SUPPORTED_EXECUTION = {
    Language.PYTHON,
}


# ==========================================================
# Public Utility Functions
# ==========================================================

def monaco_language(language: Language) -> str:
    """
    Return the Monaco Editor language identifier.

    Example
    -------
    >>> monaco_language(Language.CPP)
    'cpp'
    """

    try:
        return MONACO_LANGUAGE_MAP[language]

    except KeyError:
        raise ValueError(
            f"Unsupported Monaco language: {language}"
        )


def file_extension(language: Language) -> str:
    """
    Return the default source file extension.

    Example
    -------
    >>> file_extension(Language.PYTHON)
    '.py'
    """

    try:
        return FILE_EXTENSION_MAP[language]

    except KeyError:
        raise ValueError(
            f"No file extension defined for {language}"
        )


def display_name(language: Language) -> str:
    """
    Return a human-readable language name.

    Example
    -------
    >>> display_name(Language.PYTHON)
    'Python'
    """

    return language.value


def supports_execution(language: Language) -> bool:
    """
    Return True if the platform can execute the language.

    Note
    ----
    Monaco may support syntax highlighting for many more languages
    than the execution engine currently supports.
    """

    return language in SUPPORTED_EXECUTION


def supported_languages() -> list[Language]:
    """
    Return all languages currently available to instructors.
    """

    return list(Language)