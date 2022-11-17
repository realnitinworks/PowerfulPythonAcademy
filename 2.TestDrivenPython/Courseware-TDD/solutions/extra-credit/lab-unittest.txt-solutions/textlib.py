class BodyOfText:
    def __init__(self, text):
        self.text = text
    def num_paragraphs(self):
        if self.text == '':
            return 0
        return 1 + self.text.count('\n\n')
    def paragraphs(self):
        if self.text == '':
            return []
        return self.text.split('\n\n')

    # Here is another way to implement num_paragraphs():
    def num_paragraphs(self):
        return len(self.paragraphs())
    # The advantage of this version is that it's quick and
    # easy. You're relying on the work done in the paragraphs()
    # method, just counting how many strings are in the list it
    # returns.
    # 
    # The downside is significant, though: it's wasteful of memory and
    # CPU. This second version creates a list of strings, counts how
    # many strings are in that list, then immediately throws that list
    # away. This doesn't matter for small strings. But it starts to
    # matter a lot once you're flirting with the "big data" scale.
    # You'll understand this deeply when you go through the "Scaling
    # Python with Generators" course.
    #
    # Often, when you're writing unit tests as you develop your code,
    # you'll create a first version of the function, method, etc. that
    # just works (i.e. makes the tests pass), without thinking about
    # efficiency or even readability too much. Once you have the code
    # passing, you'll check that into version control; and then make
    # repeated passes of improving that code. And you know your
    # changes are not breaking the application, because your tests
    # continue to pass.
    #
    # So if we started writing this application with both paragraphs()
    # and num_paragraphs() from the start, we might initially use this
    # second, quick-and-easy version of num_paragraphs(); check that
    # in; then change it to the first, more-efficient version above in
    # a second commit.

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
