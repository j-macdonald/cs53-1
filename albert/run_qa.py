from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import json
import os
import random
import time
from albert import fine_tuning_utils
from albert import modeling
from albert import squad_utils
import six

#from tensorflow.contrib import cluster_resolver as contrib_cluster_resolver
#from tensorflow.contrib import tpu as contrib_tpu


class SquadExample(object):
  """A single training/test example for simple sequence classification.
     For examples without an answer, the start and end position are -1.
  """

  def __init__(self,
               qas_id,
               question_text,
               doc_tokens,
               orig_answer_text=None,
               start_position=None,
               end_position=None,
               is_impossible=False):
    self.qas_id = qas_id
    self.question_text = question_text
    self.doc_tokens = doc_tokens
    self.orig_answer_text = orig_answer_text
    self.start_position = start_position
    self.end_position = end_position
    self.is_impossible = is_impossible

  def __str__(self):
    return self.__repr__()

  def __repr__(self):
    s = ""
    s += "qas_id: %s" % (printable_text(self.qas_id))
    s += ", question_text: %s" % (
        printable_text(self.question_text))
    s += ", doc_tokens: [%s]" % (" ".join(self.doc_tokens))
    if self.start_position:
      s += ", start_position: %d" % (self.start_position)
    if self.start_position:
      s += ", end_position: %d" % (self.end_position)
    if self.start_position:
      s += ", is_impossible: %r" % (self.is_impossible)
    return s

def whitespace_tokenize(text):
    text = text.strip()
    if not text:
        return []
    tokens = text.split()
    return tokens

def is_whitespace(c):
    if c == " " or c == "\t" or c == "\r" or c == "\n" or ord(c) == 0x202F:
        return True
    return False

def printable_text(text):
  """Returns text encoded in a way suitable for print or `tf.logging`."""

  # These functions want `str` for both Python2 and Python3, but in one case
  # it's a Unicode string and in the other it's a byte string.
  if six.PY3:
    if isinstance(text, str):
      return text
    elif isinstance(text, bytes):
      return text.decode("utf-8", "ignore")
    else:
      raise ValueError("Unsupported string type: %s" % (type(text)))
  elif six.PY2:
    if isinstance(text, str):
      return text
    elif isinstance(text, unicode):
      return text.encode("utf-8")
    else:
      raise ValueError("Unsupported string type: %s" % (type(text)))
  else:
    raise ValueError("Not running on Python2 or Python 3?")


def _read_json( input_file):
    examples = []
    with tf.gfile.Open(input_file,'r') as infile:
        input_data = json.load(infile)
    questions, answers, contexts = [],[],[]
    for par in input_data['data'][0]['paragraphs']:
        ptext = par['context']
        doc_tokens = []
        char_to_word_offset = []
        prev_is_whitespace = True
        #ptext = ptext.replace('/',' ')
        for c in ptext:
            if is_whitespace(c):
                prev_is_whitespace = True
            else:
                if prev_is_whitespace:
                    doc_tokens.append(c)
                else:
                    doc_tokens[-1] += c
                prev_is_whitespace=False
            char_to_word_offset.append(len(doc_tokens)-1)

        for qa in par['qas']:
            qas_id = qa['id']
            question_text = qa['question']
            start_position = None
            end_position = None
            orig_answer_text = None
            is_impossible = False

            if is_training:
                answer = qa['answers'][0]
                orig_answer_text = answer['text']
                answer_offset = answer['answer_start']
                answer_length = len(orig_answer_text)
                start_position = char_to_word_offset[answer_offset]
                end_position = char_to_word_offset[answer_offset + answer_length - 1]
                actual_text = ' '.join(doc_tokens[start_position:(end_position+1)])
                cleaned_answer_text = ' '.join(whitespace_tokenize(orig_answer_text))
                if actual_text.find(cleaned_answer_text) == -1:
                    tf.logging.warning("Could not find answer '%s' vs. '%s'", actual_text, cleaned_answer_text)
                    continue
            else:
                start_position = -1
                end_position = -1
                orig_answer_text = ""
            example = SquadExample(
            qas_id = qas_id,
            question_text = question_text,
            doc_tokens = doc_tokens,
            orig_answer_text=orig_answer_text,
            start_position=start_position,
            end_position=end_position,
            is_impossible=False
            )
            examples.append(example)
    return examples

is_training=True
test = _read_json('./BioASQ-7b/train/Appended-Snippet/BioASQ-train-factoid-7b-snippet-2sent.json')



def build_squad_serving_input_fn(seq_length):
  """Builds a serving input fn for raw input."""

  def _seq_serving_input_fn():
    """Serving input fn for raw images."""
    input_ids = tf.placeholder(
        shape=[1, seq_length], name="input_ids", dtype=tf.int32)
    input_mask = tf.placeholder(
        shape=[1, seq_length], name="input_mask", dtype=tf.int32)
    segment_ids = tf.placeholder(
        shape=[1, seq_length], name="segment_ids", dtype=tf.int32)

    inputs = {
        "input_ids": input_ids,
        "input_mask": input_mask,
        "segment_ids": segment_ids
    }
    return tf.estimator.export.ServingInputReceiver(features=inputs,
                                                    receiver_tensors=inputs)

  return _seq_serving_input_fn

albert_hub_module_handle = None #'https://tfhub.dev/google/albert_base/3'
vocab_file = '../albert-base/assets/30k-clean.vocab'
spm_model_file = '../albert-base/assets/30k-clean.model'
do_lower_case = True

tokenizer = fine_tuning_utils.create_vocab(
    vocab_file=vocab_file,
    do_lower_case=do_lower_case,
    spm_model_file=spm_model_file,
    hub_module=albert_hub_module_handle)


squad_utils.convert_examples_to_features(
     examples=train_examples,
     tokenizer=tokenizer,
     max_seq_length=FLAGS.max_seq_length,
     doc_stride=FLAGS.doc_stride,
     max_query_length=FLAGS.max_query_length,
     is_training=True,
     output_fn=train_writer.process_feature,
     do_lower_case=do_lower_case)
