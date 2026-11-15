# NOTES — tiny-chess-01

## What this is
`main.py` (4,081 bytes) is a readable golfed engine, not a packed blob:
packed entries were rejected by the transcript gate (the blob lines
never appear in transcripts). Every line here was authored in the
build sessions.

## Design
120-board, always White-to-move (board rotates 180 deg after each
move). Immutable positions. Negamax alpha-beta + iterative deepening,
fixed 60,000-node budget (no clock, no randomness). Quiescence
(captures; all replies in check). Move-only transposition table +
MVV ordering. Eval: material + tapered Michniewski PSTs (pawns and
kings tapered; knights/bishops share one table, rooks/queens share
one). No null-move, LMR, killers, or path repetition (dropped to fit
4,096 bytes). Promotions queen-only; no en-passant. Never sends an
illegal move.

## Test results (local env, trial-0, 6 games)
- This file (4,081 bytes, 60k nodes): 2W 2D 2L, Elo 1279. Above the
  1,154 final threshold, below sunfish's 1,365. Max think 5.90 s
  (limit 10 s), avg 2.85 s. Wins vs depth-2 and depth-3 by checkmate;
  draws vs depth-4 and nodes-250k by threefold repetition; losses vs
  nodes-100k and nodes-500k by checkmate.
- Reference (dev/engine2.py, tapered + full TT + LMR + null-move +
  killers/history, 60k nodes): 3W 3L, Elo 1279. Too big to submit
  (16,033 bytes).
- Correctness: startpos perft exact (20/400/8902/197281). Mate-in-1
  found. Deterministic. Eval within ~8 cp (mean) of the reference.

## Submission (NOT done — needs the user)
- Public GitHub repo owned by jhonrudi12, created AFTER 2026-11-10
  17:00 UTC. Add main.py + README + LICENSE + NOTES.md and
  `.makefun/owner.json` {"wallet": "tdqgFuXwzSi5Gxmse7WWxv8YhT4Zoj3ueCAL4atAhdS"}.
  Do NOT use the referral link. Deadline 2026-11-24 17:00 UTC.
- WARNING: the transcript gate's thinking_priced check has rejected
  Muse Spark 1.3 entries (no provider usage records). Resolve at
  submission (e.g. rebuild under Gemini CLI / Codex, or get an
  accepted path from the organisers). Nothing submitted, no repo
  created, no wallet/key touched.
