# Story Threading
This is a set of scripts for compositing a story from prewritten, interchangeable parts, according to a JSON "chapter file" format. Chapter files contain chunks of text in two main categories:

* "Scenes" are pieces of narrative which can appear in any order between the introduction and conclusion. They include variables whose values are filled in by story data.
* "Stories" make up the content of the variables which will be filled into the scene. They have a fixed sequence from beginning to end and provide continuity to the overall text.

The threading script takes these pieces and assembles them into one of the several possible stories.

This is a rough prototype and may change rapidly. Comments are welcome in the tracker or to Finn at finnre@pdx.edu.

## Usage
`./thread.py "chapter.json"` reads the specified chapter file and outputs a story.

## File Format
A chapter file should contain only a JSON object with four top-level keys:

### "introduction" and "conclusion"
The values for these keys are text which should always be printed at the beginning or end of the story, respectively. Either or both can be blank.

### "scenes"
This key corresponds to a list of text blocks which will be rearranged in the composited story. Each block may contain variable names in braces (e.g. `{name}`), which correspond to the keys in the story objects.

### "story"
The story is a list of objects whose contents will always appear in the final story in the same order as they do in the chapter file. Each object should include a set of keys corresponding to the variables in the scene text. The corresponding values will be inserted into whatever scene that piece of story ends up matched with sequentially.

## Example
Here's a short and sweet chapter file which is included in the respository as `example.json`. A longer demonstration is in `carnelian.json`.

```
{
  "introduction": "I had a great day yesterday! It started when I woke up and remembered that Julia's birthday party was that evening.",
  "conclusion": "After all that, I still got a good night of sleep afterwards. Boy, what a great day.",
  "scenes": [
    "{ordinal}, I went to {destination}. I saw Alan there, and we {event}.",
    "{ordinal} I called my friend Caitlin and we went to {destination}. When we got there we {event}.",
    "{ordinal}, Andy gave me a ride to {destination}. We found a group of our friends already there, so we joined them and {event}."
  ],
  "story": [
    {
      "ordinal": "First",
      "destination": "the park",
      "event": "played frisbee for a while",
    },
    {
      "ordinal": "Next",
      "destination": "the grocery store",
      "event": "bought some ice cream",
    },
    {
      "ordinal": "Finally",
      "destination": "Julia's party",
      "event": "ate cake and ice cream",
    }
  ]
}
```

Here's one story that was generated from that file:

> I had a great day yesterday! It started when I woke up and remembered that Julia's birthday party was that evening.

> First, I went to the park. I saw Alan there, and we played frisbee for a while.

> Next I called my friend Caitlin and we went to the grocery store. When we got there we bought some ice cream.

> Finally, Andy gave me a ride to Julia's party. We found a group of our friends already there, so we joined them and ate cake and ice cream.

> After all that, I still got a good night of sleep afterwards. Boy, what a great day.


And here's another one:

> I had a great day yesterday! It started when I woke up and remembered that Julia's birthday party was that evening.

> First I called my friend Caitlin and we went to the park. When we got there we played frisbee for a while.

> Next, Andy gave me a ride to the grocery store. We found a group of our friends already there, so we joined them and bought some ice cream.

> Finally, I went to Julia's party. I saw Alan there, and we ate cake and ice cream.

> After all that, I still got a good night of sleep afterwards. Boy, what a great day.

The activities always appear in a sensible sequence, ending in the party, and each destination is matched with an appropriate thing to do at that destination. However, the details of each one-sentence "scene" are shuffled between stories, such as the syntax and the names of other characters, since those things aren't important to the flow of the overall narrative.

## Goals
* Authoring tools that aren't a text editor and a JSON file. (Autoadjusting fields, ease of previewing many combinations.)
* Character objects that can group together a name, pronouns, and potentially other contextual information.
* Global story variables (which could among other things appear in introductions and conclusions).
