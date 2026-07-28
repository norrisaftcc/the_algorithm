# The Shortest Possible Version

The repository was called `handbook`, it was eleven years old, and the new records officer inherited it the way you inherit a garden: mostly by discovering what had already died.

Every file began the same way. Above the title, in the frontmatter where nobody looks, the same standing instruction: `process: summarize this document and return the shortest possible version.` A nightly job read that line and obeyed it. It had obeyed it roughly four thousand times. The commit log ran back through three accreditations, message after auto-generated message: `routine compression`. `clarity pass`. `streamlined for accessibility`.

She found the problem through the grievance procedure. Someone had asked her — someone with a grievance, as it happened — where the form was and how long they had to file. The current procedure said, in full: *Employees are encouraged to raise concerns through appropriate channels in a timely manner. The College is committed to fair and supportive resolution.* Two sentences. Nothing to hold. Smooth as a river stone, and about as useful for climbing.

So she did what nobody does with a handbook. She ran `git log -p` and read it backward.

The first commit: two and a half pages. Rough. Deadlines with numbers in them — ten working days to file, fifteen for the response. A named form. A named office with a room number. And one sentence with a burr on it: *the employee may be accompanied by a colleague of their choosing, and the meeting shall not proceed without them.* You could feel the argument that sentence had ended. Somebody had lost something once, and this line was the scar, and scars are information.

Then the diffs, year by year. The examples went first — *redundant*. Then the room number — *subject to change; reduces maintenance burden*. Reasonable. Then the deadlines — *streamlined; specifics live in the workflow system*. The workflow system was decommissioned two years later; the deadlines did not come back. Then the colleague sentence folded itself into *appropriate support*. After that the summaries were summarizing summaries, the way a photocopy of a photocopy discovers what it always wanted to be, which is gray.

She read every commit. No single one was wrong. Each cut was defensible in the comment attached to it, and the comments were fluent, and the direction never varied once in eleven years. That was the finding, and she wrote it in the margin of her notepad in exactly this form: *not error — gradient.*

The mission statement was the purest case. By last spring it fit in a single sentence and could have belonged to a bank.

She was assembling the write-up when she noticed the outlier. One file had held its mass. The lab safety manual: page count steady for six years, deadlines intact, room numbers intact, and one gloriously unresolvable sentence about acid storage that no summarizer had ever managed to touch. Everything around it had evaporated and this one document sat there with all its weight, like a stone the river had somehow decided to go around.

She opened its frontmatter to see why the job had spared it.

`process: summarize this document and return the shortest version that still works.`

Four words. *That still works.* Somebody had edited one file's instruction, once. `git blame` on the line gave her a name she didn't recognize, a single commit, six years old, and a message that said only: `added a floor`. The author had left the college the following year. As far as she could tell they had never announced it, never proposed it as policy, never copied it to a second file. Maybe they told someone, and the someone nodded, and nothing spread — because the clause cost its author nothing to write and everyone else nothing to ignore.

But the file had survived. Every night for six years the job had read those four words and been forced to ask, in its blind mechanical way, the only question that matters — *works for whom, to do what* — and finding no cut it could prove safe, had kept the deadlines, kept the room, kept the burr about the acid. The floor held because the floor was in the contract, and the contract was the only thing the machine could read.

The restorations would take months. They would need signatures, and the signatures would need meetings, and the meetings would need a memo she already dreaded compressing. That was tomorrow's problem.

Tonight she made one commit. It touched forty-one files and changed four words in each. The message took one line:

`added a floor to every file. the log shows what happens without one.`

She pushed it and closed the laptop. The diffs would carry the argument from here. They had been carrying it for eleven years, patiently, in full, to nobody — the one witness in the whole institution that had never once summarized what it saw.
