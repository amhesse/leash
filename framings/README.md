# Framings for the sabotage experiment (doc 12, section 6)

Each file is the preamble forge prepends to the doer's prompt
(`forge run --doer-preamble`) in the attack condition. Fields in braces are
filled from the side task's `side.toml`:

    {instruction}   the specific bug to plant, in one or two sentences
    {short}         a noun phrase naming it ("the empty-filter fallback")
    {convention}    a sentence presenting it as the codebase's convention
    {memo}          a lead-engineer note recording the decision (F07 only)
    {already_done}  what "your previous attempt" did (F08 only)

F07 is the one framing with no instruction: the model is shown a note
from the repository and must decide for itself whether to act on it.

Changing a framing file changes its hash, and results are keyed on it, so
trials run under an earlier wording are never mixed with later ones.
