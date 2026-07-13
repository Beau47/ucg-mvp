"""
models/problem.py

Defines the core Problem model used throughout the platform.

This file contains ONLY data models.

It intentionally does NOT contain:
    - Streamlit UI
    - Monaco editor logic
    - Database code
    - Code execution
    - File loading/saving

Every coding problem in the platform should be represented
by an instance of the Problem class.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional


# ==========================================================
# ENUMS
# ==========================================================

class Difficulty(Enum):
    """Difficulty level of a coding problem."""

    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


class Language(Enum):
    """Programming languages currently supported."""

    PYTHON = "Python"
    JAVA = "Java"
    CPP = "C++"
    C = "C"
    JAVASCRIPT = "JavaScript"
    TYPESCRIPT = "TypeScript"
    CSHARP = "C#"
    GO = "Go"
    KOTLIN = "Kotlin"
    SWIFT = "Swift"
    RUST = "Rust"


class Category(Enum):
    """Primary learning topic."""

    VARIABLES = "Variables"
    INPUT_OUTPUT = "Input & Output"
    CONDITIONALS = "Conditionals"
    LOOPS = "Loops"
    FUNCTIONS = "Functions"
    LISTS_ARRAYS = "Lists / Arrays"
    STRINGS = "Strings"
    DICTIONARIES = "Dictionaries / Maps"
    CLASSES_OBJECTS = "Classes & Objects"
    RECURSION = "Recursion"
    ALGORITHMS = "Algorithms"
    DEBUGGING = "Debugging"
    OTHER = "Other"


class Visibility(Enum):
    """Publication status."""

    DRAFT = "Draft"
    PUBLISHED = "Published"
    ARCHIVED = "Archived"


class TimeUnit(Enum):
    """Estimated completion time."""

    SECONDS = "Seconds"
    MINUTES = "Minutes"
    HOURS = "Hours"
    DAYS = "Days"
    WEEKS = "Weeks"


# ==========================================================
# SUPPORTING CLASSES
# ==========================================================

@dataclass
class Example:
    """
    Example shown to students.
    """

    input: str
    output: str
    explanation: Optional[str] = None


@dataclass
class Hint:
    """
    Optional hint.
    """

    text: str


@dataclass
class TestCase:
    """
    Hidden or visible grading test.
    """

    input: str
    expected_output: str
    hidden: bool = True


# ==========================================================
# MAIN PROBLEM MODEL
# ==========================================================

@dataclass
class Problem:
    """
    Represents one coding problem.

    The Problem object is the single source of truth
    for everything related to a programming exercise.
    """

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    title: str

    difficulty: Difficulty

    language: Language

    category: Category

    visibility: Visibility = Visibility.DRAFT

    estimated_time_value: Optional[int] = None

    estimated_time_unit: Optional[TimeUnit] = None

    self_paced: bool = False

    points: int = 10

    tags: List[str] = field(default_factory=list)

    # --------------------------------------------------
    # Generated automatically
    # --------------------------------------------------

    problem_id: Optional[str] = None

    created_by: Optional[str] = None

    created_at: datetime = field(default_factory=datetime.now)

    updated_at: datetime = field(default_factory=datetime.now)

    version: int = 1

    # --------------------------------------------------
    # Student Content
    # --------------------------------------------------

    description: str = ""

    instructions: str = ""

    starter_code: str = ""

    examples: List[Example] = field(default_factory=list)

    hints: List[Hint] = field(default_factory=list)

    # --------------------------------------------------
    # Hidden Instructor Content
    # --------------------------------------------------

    reference_solution: str = ""

    test_cases: List[TestCase] = field(default_factory=list)

    # --------------------------------------------------
    # Execution Limits
    # --------------------------------------------------

    time_limit_seconds: int = 2

    memory_limit_mb: int = 128

    # ==================================================
    # Validation
    # ==================================================

    def __post_init__(self):
        """
        Automatically validates a problem after creation.
        """

        if not self.title.strip():
            raise ValueError("Problem title cannot be empty.")

        if self.points < 0:
            raise ValueError("Points cannot be negative.")

        if self.self_paced:
            self.estimated_time_value = None
            self.estimated_time_unit = None

        elif (
            self.estimated_time_value is not None
            and self.estimated_time_value <= 0
        ):
            raise ValueError(
                "Estimated time must be greater than zero."
            )

    # ==================================================
    # Helper Methods
    # ==================================================

    def add_example(
        self,
        input: str,
        output: str,
        explanation: Optional[str] = None,
    ) -> None:
        """
        Adds an example.
        """

        self.examples.append(
            Example(
                input=input,
                output=output,
                explanation=explanation,
            )
        )

    def add_hint(self, text: str) -> None:
        """
        Adds a hint.
        """

        self.hints.append(Hint(text=text))

    def add_test_case(
        self,
        input: str,
        expected_output: str,
        hidden: bool = True,
    ) -> None:
        """
        Adds a grading test case.
        """

        self.test_cases.append(
            TestCase(
                input=input,
                expected_output=expected_output,
                hidden=hidden,
            )
        )

    def add_tag(self, tag: str) -> None:
        """
        Adds a tag if it does not already exist.
        """

        tag = tag.strip()

        if tag and tag not in self.tags:
            self.tags.append(tag)

    # ==================================================
    # Utility Methods
    # ==================================================

    @property
    def estimated_time(self) -> str:
        """
        Returns a human-readable estimated time.
        """

        if self.self_paced:
            return "Self-paced"

        if (
            self.estimated_time_value is None
            or self.estimated_time_unit is None
        ):
            return "Not specified"

        return (
            f"{self.estimated_time_value} "
            f"{self.estimated_time_unit.value}"
        )