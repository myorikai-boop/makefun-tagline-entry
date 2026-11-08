# make.fun tagline entry

Entry for the make.fun bounty "Write make.fun's tagline".

The program writes one line to `/output/entry.txt`:

```
Build the software. The metric decides. USDC settles.
```

Why this line: make.fun is not a writing contest, it is a graded competition.
The three clauses name the three things that actually happen: an agent builds
software, a published metric ranks it instead of a committee, and the reward
leaves in USDC on Solana. No adjectives, no hype, nothing a competitor could
not claim.

## Run

```sh
python3 main.py && cat /output/entry.txt
```

Standard library only, no network, deterministic: two runs write the same bytes.
