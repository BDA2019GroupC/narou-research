# coding: utf-8
import json
import logging

logging.basicConfig(format='[%(levelname)s] %(name)s: %(message)s',
                    level = logging.WARN)
logger = logging.getLogger(__name__)

class Processor(object):
    def __init__(self, stream_in, stream_out):
        """ Initialize and reset this instance
        Args:
            stream_in  : Input stream
            stream_out : Output stream
        """
        self.threshold = 0
        self.stream_in = stream_in
        self.stream_out = stream_out

    def preprocess(self, depth=0):
        """ Process input lines and output results
        This method reads input stream line by line and
        passes them to _preprocess, which formats a line
        and returns one or more formatted sentences.
        (Be noticed line may contain multiple sentences.)
        """
        while True:
            line = self.stream_in.readline()
            if line == '': break
            
            logger.info("Processing: {}".format(line.strip()))

            for sentence in self._preprocess(line.strip(), depth):
                self.stream_out.write(sentence.strip() + '\n')

    def _preprocess(self, line, depth=0):
        """ Yield formatted sentences
        Args:
            line (str): A line of sentence(s)

        Yields:
            str: Formatted sentence
        """
        line = self._remove_ruby(line)
        
        # Process conversation
        for conv in self._process_conversations(line, depth):
            # Split line into sentences
            for sentence in self._split_line(conv):
                if len(sentence) > 1:
                    yield sentence
                    
    def _remove_ruby(self, line):
        newLine = ''
        begin_ruby = False
        for c in line:
            if c == '《':
                begin_ruby = True
            if not begin_ruby:
                newLine += c
            if c == '》':
                begin_ruby = False
        return newLine
    
    def _process_conversations(self, line, depth):
        """ Extract conversations and pass them to _preprocess
        """
        bracketsList = [
            ('「', '」'), ('『', '』'), ('【', '】'),
            ('（', '）'), ('［', '］'), ('〈', '〉'),
            ('｛', '｝'), ('〔', '〕'),
            ('〘', '〙'), ('〚', '〛'), ('«', '»'),
            ('”', '”'), ('"', '"'), ('“', '”'),
            ('(', ')'), ('[', ']'), ('<', '>'),
        ]
        beginTalk = False
        bracketType = None
        newLine = ''
        prevNewLine = ''
        flush = False
        
        for c in line:
            for brackets in bracketsList:
                if not beginTalk and c == brackets[0]:
                    # found the beginning of conversation
                    prevNewLine = newLine
                    #yield newLine
                    #yield brackets[0]
                    beginTalk = True
                    bracketType = brackets
                    newLine = ''
                    break
                
                elif beginTalk and c == bracketType[1]:
                    # found the end of conversation
                    # we need to preprocess this line recursively
                    # since it's conversation
                    if len(newLine) >= 8:
                        if flush:
                            yield prevNewLine
                            flush = False
                        else:
                            for sentence in self._split_line(prevNewLine):
                                yield sentence
                        for sentence in self._split_line(newLine):
                            yield sentence
                        newLine = ''
                    else:
                        newLine = prevNewLine + bracketType[0] + newLine + bracketType[1]
                        flush = True
                    #for sentence in self._preprocess(newLine, depth + 1):
                    #    yield sentence
                    #yield bracketType
                    beginTalk = False
                    break
                
            else:
                # if c is not a bracket
                newLine += c

        for brackets in bracketsList:
            if newLine.strip():
                if newLine[0] == brackets[0] and newLine[-1] == brackets[1]:
                    newLine = newLine[1:-1]
                elif newLine[-1] == brackets[1]:
                    newLine = newLine[:-1]
        yield newLine

    def _split_line(self, line):
        periodList = [
            '。', '．', '.', '…',
            '！', '？', '⁉', '⁈', '!', '?',
        ]
        bracketsList = [
            ('「', '」'), ('『', '』'), ('【', '】'),
            ('（', '）'), ('［', '］'), ('〈', '〉'),
            ('｛', '｝'), ('《', '》'), ('〔', '〕'),
            ('〘', '〙'), ('〚', '〛'), ('«', '»'),
            ('”', '”'), ('"', '"'), ('“', '”'),
            ('(', ')'), ('[', ']'), ('<', '>'),
        ]
        sentences = []
        newLine = ''
        
        for c in line:
            newLine += c
            for period in periodList:
                if c == period:
                    if len(newLine) == 1 and len(sentences) > 0:
                        sentences[-1] += c
                    else:
                        sentences.append(newLine)
                    newLine = ''
            for brackets in bracketsList:
                if c == brackets[1]:
                    if len(newLine) > 2:
                        if newLine[-2] in periodList:
                            sentences.append(newLine)
                            newLine = ''
                    elif len(sentences) > 0:
                        sentences[-1] += c
                        sentences[-1] = sentences[-1][1:-1]
                        newLine = ''
                            
        if newLine != '':
            sentences.append(newLine)
        
        return sentences
