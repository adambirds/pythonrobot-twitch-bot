from typing import List

from zulint.custom_rules import Rule, RuleList

trailing_whitespace_rule: "Rule" = {
    "pattern": r"\s+$",
    "strip": "\n",
    "description": "Fix trailing whitespace",
}
whitespace_rules: List["Rule"] = [
    # This linter should be first since bash_rules depends on it.
    trailing_whitespace_rule,
]

markdown_whitespace_rules: List["Rule"] = [
    *(rule for rule in whitespace_rules if rule["pattern"] != r"\s+$"),
    # Two spaces trailing a line with other content is okay--it's a Markdown line break.
    # This rule finds one space trailing a non-space, three or more trailing spaces, and
    # spaces on an empty line.
    {
        "pattern": r"((?<!\s)\s$)|(\s\s\s+$)|(^\s+$)",
        "strip": "\n",
        "description": "Fix trailing whitespace",
    },
    {
        "pattern": "^#+[A-Za-z0-9]",
        "strip": "\n",
        "description": "Missing space after # in heading",
        "good_lines": ["### some heading", "# another heading"],
        "bad_lines": ["###some heading", "#another heading"],
    },
]

markdown_rules = RuleList(
    langs=["md"],
    rules=[
        *markdown_whitespace_rules,
        {
            "pattern": r"\[(?P<url>[^\]]+)\]\((?P=url)\)",
            "description": "Linkified Markdown URLs should use cleaner <http://example.com> syntax.",
        },
        {
            "pattern": r"\][(][^#h]",
            "description": "Use absolute links from docs served by GitHub",
        },
    ],
    max_length=120,
)

non_py_rules = [
    markdown_rules,
]
