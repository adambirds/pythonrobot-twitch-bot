# Commit Guidelines

## Commit Discipline

We follow the Git project's own commit discipline practice of "Each
commit is a minimal coherent idea". This discipline takes a bit of work,
but it makes it much easier for code reviewers to spot bugs, and
makes the commit history a much more useful resource for developers
trying to understand why the code works the way it does, which also
helps a lot in preventing bugs.

Commits must be coherent:

*   It should pass tests (so test updates needed by a change should be
    in the same commit as the original change, not a separate "fix the
    tests that were broken by the last commit" commit).
*   It should be safe to deploy individually, or explain in detail in
    the commit message as to why it isn't (maybe with a [manual] tag).
*   Error handling should generally be included along with the code that
    might trigger the error.
*   TODO comments should be in the commit that introduces the issue or
    the functionality with further work required.

Commits should generally be minimal:

*   Significant refactoring should be done in a separate commit from
    functional changes.
*   Moving code from one file to another should be done in a separate
    commits from functional changes or even refactoring within a file.
*   2 different refactoring should be done in different commits.
*   2 different features should be done in different commits.
*   If you find yourself writing a commit message that reads like a list
    of somewhat dissimilar things that you did, you probably should have
    just done multiple commits.

When not to be overly minimal:

*   For completely new features, you don't necessarily need to split out
    new commits for each little subfeature of the new feature. E.g., if
    you're writing a new tool from scratch, it's fine to have the
    initial tool have plenty of options/features without doing separate
    commits for each one. That said, reviewing a 2000-line giant blob of
    new code isn't fun, so please be thoughtful about submitting things
    in reviewable units.

Other considerations:

*   Overly fine commits are easy to squash later, but not vice versa.
    So err toward small commits, and the code reviewer can advise on
    squashing.
*   If a commit you write doesn't pass tests, you should usually fix
    that by amending the commit to fix the bug, not writing a new "fix
    tests" commit on top of it.

We expect you to structure the commits in your pull requests to form
a clean history before we will merge them.  It's best to write your
commits following these guidelines in the first place, but if you don't,
you can always fix your history using `git rebase -i`.

Never mix multiple changes together in a single commit, but it's great
to include several related changes, each in their own commit, in a
single pull request.  If you notice an issue that is only somewhat
related to what you were working on, but you feel that it's too minor
to create a dedicated pull request, feel free to append it as an
additional commit in the pull request for your main project (that
commit should have a clear explanation of the bug in its commit
message).  This way, the bug gets fixed, but this independent change
is highlighted for reviewers.  Or just create a dedicated pull request
for it.  Whatever you do, don't squash unrelated changes together in a
single commit; the reviewer will ask you to split the changes out into
their own commits.

It can take some practice to get used to writing your commits with a
clean history so that you don't spend much time doing interactive
rebases. For example, often you'll start adding a feature, and discover
you need to do a refactoring partway through writing the feature. When that
happens, we recommend you stash your partial feature, do the refactoring,
commit it, and then unstash and finish implementing your feature.

## Commit messages

The first line of the commit message is the **summary**. The summary:
* is written in the imperative (e.g., "Fix ...", "Add ...")
* is kept short (max 76 characters, ideally less), while concisely
  explaining what the commit does
* is clear about what part of the code is affected -- often by prefixing
  with the name of the subsystem and a colon, like "ci: ..." or "docs: ..."
* is a complete sentence.

### Good summaries:

Below is an example of a good commit summary line.  It starts with the
prefix "docs:", using lowercase "**d**".  Next, "Add codecov badge to
README.md." starts with a capital "**A**", uses imperative tense,
and ends with a period.

> docs: Add codecov badge to README.md.

Here are some more positive examples:

> ci: Add workflow to publish package to PyPI.

> lint: Add black linter to lint tool.

The summary is followed by a blank line, and then the body of the
commit message.

### Message body:

*   The body is written in prose, with full paragraphs; each paragraph should
    be separated from the next by a single blank line.
*   The body explains:
    *   why and how the change was made
    *   any manual testing you did in addition to running the automated tests
    *   any aspects of the commit that you think are questionable and
        you'd like special attention applied to.
*   When you fix a GitHub issue, [mark that you've fixed the issue in
    your commit
    message](https://help.github.com/en/articles/closing-issues-via-commit-messages)
    so that the issue is automatically closed when your code is merged.
    Our preferred style for this is to have the final paragraph of
    the commit message read e.g. "Fixes: \#123.".
*   Avoid `Partially fixes #1234`; GitHub's regular expressions ignore
    the "partially" and close the issue. `Fixes part of #1234` is a good alternative.
*   Any paragraph content in the commit message should be line-wrapped
    to about 68 characters per line, but no more than 70, so that your
    commit message will be reasonably readable in `git log` in a normal
    terminal. You may find it helpful to:
    *   configure Git to use your preferred editor, with the EDITOR
        environment variable or `git config --global core.editor`, and
    *   configure the editor to automatically wrap text to 70 or fewer
        columns per line (all text editors support this).
