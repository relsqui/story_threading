# Story Threading
This is a set of scripts for compositing a story from prewritten, interchangeable parts, according to a JSON "chapter file" format. Chapter files contain chunks of text in two main categories:

* "Scenes" are pieces of narrative which can appear in any order between the introduction and conclusion. They include variables whose values are filled in by story data.
* "Stories" make up the content of the variables which will be filled into the scene. They have a fixed sequence from beginning to end and provide continuity to the overall text.

They may also contain information about characters that can be inserted into the story at appropriate points. The threading script takes all of these pieces and assembles them into one of the several possible stories.

This is a rough prototype and may change rapidly. Comments are welcome in the tracker or to Finn at finnre@pdx.edu.

## Usage
`./thread.py "chapter.json"` reads the specified chapter file and outputs a story.

## File Format
A chapter file should contain only a JSON object with at least four top-level keys:

### "introduction" and "conclusion"
The values for these keys are text which should always be printed at the beginning or end of the story, respectively. Either or both can be blank.

### "scenes"
This key corresponds to a list of text blocks which will be rearranged in the composited story. Each block may contain variable names in braces (e.g. `{someone}`), which correspond to the keys in the story objects.

When the variable name corresponds to a character in the story, it will be replaced with the character's name. If the variable is followed by a period and a form of "they," it will be replaced with the corresponding pronoun which is applicable to that character. For example, if the variable name `someone` corresponds to a character named Izzy whose pronouns are she, her, etc. then:

* `{someone}` will be replaced with "Izzy"
* `{someone.they}` will be replaced with "she"
* `{someone.themselves}` will be replaced with "herself"

and so on. ("They" is used as the generic, not only because it's gender-neutral, but because all of its forms are unique, unlike either "he" or "she.") The pronoun markers can be title-cased, in which case the resulting pronoun will also be.

* `{someone.Theirs}` will be replaced with "Hers"
* `{someone.Them}` will be replaced with "Her"

### "story"
The story is a list of objects whose contents will always appear in the final story in the same order as they do in the chapter file. Each object should include a set of keys corresponding to the variables in the scene text. The corresponding values are treated in one of two ways, depending on their type:

* String values simply replace the variable name in the scene.
* Integer values are mapped to the corresponding story character (see below). The variable name by itself will be replaced with the character's name. It can be followed by a pronoun to be replaced with the appropriate pronoun (see above).

The story threader will always try to match up scenes to story in such a way that the story provides at least the correct set of variables to fill in the scene. (It may also contain extras.) If such a scene isn't available, it will stop with an error.

### Optional: "characters"
If present, this key should hold a list of objects, each of which has two properties.

* `"name"` can be any string.
* `"pronouns"` should be one of: "he" "she" or "they" (case insensitive)

Each character is referred to by their index in this list. (The first character is 0, then 1, 2, etc.) When a scene contains a variable that corresponds to an integer value in the story, that value will be replaced by the appropriate character's name. Generic pronouns can also be added and will be replaced by the appropriate pronoun for the character; see "scenes" above.

## Example
The following story was generated from the [example chapter file](chapters/example.json) included in the repository.

> I had a great day yesterday! It started when I woke up and remembered that Julia's birthday party was that evening.
> First, Alan gave me a ride to the park. We found a group of our friends already there, so we joined them. He read a book, and I practiced freethrows.
> Next I called my friend Andy and we went to the grocery store. When we got there, he bought some ice cream while I picked out a cake.
> Finally, I went to Julia's party. I saw Caitlin there, and she and I ate cake and ice cream.
> After all that, I still got a good night of sleep afterwards. Boy, what a great day.

Here's another story from the same chapter file. The pieces in the story section (destinations, names, and activities) remain in the same order, but the structures from the scene section are shuffled around.

> I had a great day yesterday! It started when I woke up and remembered that Julia's birthday party was that evening.
> First, I went to the park. I saw Alan there, and he and I practiced freethrows.
> Next, Andy gave me a ride to the grocery store. We found a group of our friends already there, so we joined them. He picked out a cake, and I bought some ice cream.
> Finally I called my friend Caitlin and we went to Julia's party. When we got there, she ate cake and ice cream while I danced.
> After all that, I still got a good night of sleep afterwards. Boy, what a great day.

## Goals
* Authoring tools that aren't a text editor and a JSON file. (Autoadjusting fields, ease of previewing many combinations.)
  * Stop using JSON altogether so we can put more semantics in the savefiles. Related to the above because there still has to be a nice way for humans to create the files.
* ~~Character objects that can group together a name, pronouns, and potentially other contextual information.~~
* Global story variables (which could among other things appear in introductions and conclusions).
