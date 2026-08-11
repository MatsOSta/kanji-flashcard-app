# AGENTS.md

## Project

`kanji-flashcard-app` is a learning-focused side project for building a kanji flashcard application.

The project should be developed incrementally. Prefer small, understandable changes over large framework or architecture additions.

## Working principles

* Keep changes focused on the task requested.
* Do not introduce unnecessary abstractions or dependencies.
* Prefer simple, readable Python over clever implementations.
* Do not rewrite unrelated code while completing a task.
* Preserve existing behavior unless the task explicitly requires changing it.
* Explain important design decisions when they are not obvious.

## Learning focus

This repository is also being used to learn software development and engineering practices.

When implementing non-trivial changes:

* Prefer solutions that are easy to understand and discuss.
* Avoid hiding important logic behind generated boilerplate.
* Point out relevant engineering concepts, trade-offs, and alternatives.
* Do not over-engineer the project in anticipation of future requirements.

## Git

* Do not commit changes unless explicitly asked.
* Do not push changes unless explicitly asked.
* Do not create or delete branches unless explicitly asked.
* Keep commits focused and use descriptive commit messages.
* Before proposing a commit, summarize the files changed and the purpose of the change.

## Dependencies

* Do not add new runtime or development dependencies without explaining why they are needed.
* Prefer the Python standard library when it is reasonable.
* Keep dependency versions reproducible when dependency management is introduced.

## Testing

When modifying application logic:

* Add or update tests where appropriate.
* Run the relevant tests before reporting completion.
* Report any tests that could not be run and why.

## Validation

Before considering a task complete:

* Review the resulting diff.
* Check for unrelated changes.
* Run relevant tests or validation commands.
* Summarize what changed, important design decisions, and any remaining limitations.

