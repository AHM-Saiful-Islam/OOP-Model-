"""
Implementing a Document model for analysis
Background
We work more with digital documents now-a-days than paper books. A digital document is 
easy to read in devices and easy to preserve and analyze. Assume that you are preparing a 
system that preserves and analyzes such documents. Each document can be in any format –
MS Word, PDF, epub etc. For the sake of analyzing the documents we need to extract the 
information of the documents.
For the sake of simplicity let us assume the following data structure for each document.
Each document is represented by an object that holds information like Name of it, file 
format, author, date of publication. The content of document is structured in a tree 
structure where the topmost node could be a Chapter or Section heading, which then may 
contain another Chapter or section heading or some text. If we take this file, as an example, 
it has a heading, followed by another heading, followed by texts.
Task
1. Prepare a simplified object-oriented model to represent documents.

Some points to think
1. What would be your approach for testing your implementation?
2. Have you initially estimated how much time you will need for the task? Have you 
needed more or less? What could be the possible reason of the differences between 
your estimation and reality?
3. Can you think of some modifications to your model? Which additional benefits these 
modifications will bring

"""


class Document:
    def __init__(self, name, format, author, date):
        self.name = name
        self.format = format
        self.author = author
        self.date = date
        self.content = []


class Node:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.children = []


class Chapter(Node):
    def __init__(self, value):
        super().__init__("Chapter", value)


class Section(Node):
    def __init__(self, value):
        super().__init__("Section", value)


class Text(Node):
    def __init__(self, value):
        super().__init__("Text", value)


'''
Test the implementation
'''

document = Document("Sample Document", "pdf", "Saiful", "10/02/2021")

chapter1 = Chapter("Chapter 1")
section1 = Section("Section 1.1")
text1 = Text("This is sample text.")
section1.children.append(text1)
chapter1.children.append(section1)
document.content.append(chapter1)

print("Document name:", document.name)
print("Author:", document.author)
print("Date:", document.date)
print("Content:")
for node in document.content:
    print(" -", node.value)
    for child in node.children:
        print("   -", child.value)

'''
 1. Testing the Implementation

We test the implementation by creating a Document object and adding Chapter, Section, Text
 objects to it to represent its contents.

 2.  Time Estimation

I initially estimated that this task would take about an 3 to complete, but it
 actually took me around 5 hours to complete the implementation. The reason for
 this difference is that the model was different than I thought.

 3.  Possible Modifications to the Model

To improve the model, we can add more attributes to the Document class to store
 additional information about the document, such as the number of pages, the language,
 and the subject. We can also add a method to extract the text from the document and
 analyze it, such as counting the number of words, finding the most common words, etc.
 These modifications will help us to analyze the documents more effectively and efficiently.
'''