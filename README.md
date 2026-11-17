# Talking Avi

A Talking-Tom style app starring Avi. Talk to him and he repeats it in a funny voice; poke, tickle, feed and dance with him.

The whole app is one self-contained file: `index.html` (about 290 KB, no internet needed once loaded).

## Run it

- **Voice repeat needs the microphone**, so open it from an `https://` address (GitHub Pages, Netlify, any host) in Chrome or Safari. Opening the file directly or inside an app preview may block the mic. Typing words for Avi works everywhere.
- On a phone, use *Add to Home Screen* to launch it like an app.

## Features

- Repeats your voice with lip-sync: Baby Avi, Chipmunk, Giant and Robot voices, adjustable mic sensitivity
- Tap reactions: head, nose, cheeks, belly, heart, hands, legs; swipe his face to spin him
- Buttons: Milk, Cake, Toot, Tickle, Dance, Bubbles, Love, Sleep
- Blinks, looks around, follows your finger, yawns when bored and falls asleep
- Records a video with sound

## Editing

`index.html` is generated. Edit `src/app.src.html` (assets are referenced as `__AVI__`, `__F500__`, etc.) and rebuild:

```
python3 src/build.py
```

`src/assets/` holds the cut-out photo (`avi.webp`), icons and the Fredoka font subsets.

## Credits

- Character rendering: WebGL warp of the cut-out photo (blinks, mouth, head motion); all sounds are synthesised in code with Web Audio.
- Font: [Fredoka](https://github.com/google/fonts/tree/main/ofl/fredoka), SIL Open Font License 1.1.
