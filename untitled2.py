# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:33:02 2023

@author: HP
"""
'''
import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Attention
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
import numpy as np

loaded_model = tf.keras.models.load_model("english_to_marathi_translation_model")

###########################################
import tensorflow as tf

# Load the model
loaded_model = tf.keras.models.load_model("english_to_marathi_translation_model")

# Sample input text in English
input_text = ["How are you doing?"]

# Tokenize and pad the input sequence
input_seq = loaded_model.input[0].numpy()
input_seq = loaded_model.input[0].tokenizer.texts_to_sequences(input_text)
input_seq = loaded_model.input[0].tokenizer.pad_sequences(input_seq)

# Initialize the decoder input with a start token
decoder_input = tf.expand_dims([loaded_model.input[1].tokenizer.word_index["<start>"]], 0)

# Initialize the hidden state of the encoder with zeros
encoder_states = [tf.zeros((1, loaded_model.input[0].shape[1])), tf.zeros((1, loaded_model.input[0].shape[1]))]

# Initialize a list to store the Marathi translation
output_text = []

# Maximum length for the output sequence
max_length = loaded_model.input[1].shape[1]

# Perform inference
for _ in range(max_length):
    # Predict the next word in the sequence
    predictions = loaded_model.predict([input_seq, decoder_input, encoder_states])

    # Get the index of the predicted word
    predicted_index = tf.argmax(predictions, axis=-1).numpy()[0, 0]

    # Break if the end token is predicted
    if loaded_model.input[1].tokenizer.index_word[predicted_index] == "<end>":
        break

    # Add the predicted word to the output sequence
    output_text.append(loaded_model.input[1].tokenizer.index_word[predicted_index])

    # Update the decoder input for the next iteration
    decoder_input = tf.expand_dims([predicted_index], 0)

# Print the translated output
print("Input English Text:", input_text[0])
print("Translated Marathi Text:", " ".join(output_text))
'''
'''
import tensorflow as tf

# Load the saved model
loaded_model = tf.keras.models.load_model("english_to_marathi_translation_model")

# Function for performing inference
def translate_sentence(input_text):
    # Tokenize and pad the input sequence
    input_seq = loaded_model.input[0].tokenizer.texts_to_sequences([input_text])
    input_seq = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=loaded_model.input[0].shape[1])

    # Initialize the decoder input with a start token
    start_token = loaded_model.input[1].tokenizer.word_index["<start>"]
    decoder_input = tf.expand_dims([start_token], 0)

    # Initialize the hidden state of the encoder with zeros
    encoder_states = [tf.zeros((1, loaded_model.input[0].shape[1])), tf.zeros((1, loaded_model.input[0].shape[1]))]

    # Initialize a list to store the Marathi translation
    output_text = []

    # Maximum length for the output sequence
    max_length = loaded_model.input[1].shape[1]

    # Perform inference
    for _ in range(max_length):
        # Predict the next word in the sequence
        predictions = loaded_model.predict([input_seq, decoder_input] + encoder_states)

        # Get the index of the predicted word
        predicted_index = tf.keras.backend.eval(tf.argmax(predictions, axis=-1))[0, 0]

        # Break if the end token is predicted
        if loaded_model.input[1].tokenizer.index_word[predicted_index] == "<end>":
            break

        # Add the predicted word to the output sequence
        output_text.append(loaded_model.input[1].tokenizer.index_word[predicted_index])

        # Update the decoder input for the next iteration
        decoder_input = tf.expand_dims([predicted_index], 0)

    # Return the translated text
    return " ".join(output_text)

# Example usage
input_sentence = "How are you doing?"
translated_sentence = translate_sentence(input_sentence)

print(f"Input English Text: {input_sentence}")
print(f"Translated Marathi Text: {translated_sentence}")
'''
'''
import tensorflow as tf

# Load the saved model
loaded_model = tf.keras.models.load_model("english_to_marathi_translation_model")

# Function for translating a sentence
def translate_sentence(input_text):
    # Tokenize and pad the input sequence
    input_seq = loaded_model.input[0].tokenizer.texts_to_sequences([input_text])
    input_seq = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=loaded_model.input[0].shape[1])

    # Initialize the decoder input with a start token
    start_token = loaded_model.input[1].tokenizer.word_index["<start>"]
    decoder_input = tf.expand_dims([start_token], 0)

    # Initialize the hidden state of the encoder with zeros
    encoder_states = [tf.zeros((1, loaded_model.input[0].shape[1])), tf.zeros((1, loaded_model.input[0].shape[1]))]

    # Initialize a list to store the Marathi translation
    output_text = []

    # Maximum length for the output sequence
    max_length = loaded_model.input[1].shape[1]

    # Perform inference
    for _ in range(max_length):
        # Predict the next word in the sequence
        predictions = loaded_model.predict([input_seq, decoder_input] + encoder_states)

        # Get the index of the predicted word
        predicted_index = tf.argmax(predictions, axis=-1).numpy()[0, 0]

        # Break if the end token is predicted
        if loaded_model.input[1].tokenizer.index_word[predicted_index] == "<end>":
            break

        # Add the predicted word to the output sequence
        output_text.append(loaded_model.input[1].tokenizer.index_word[predicted_index])

        # Update the decoder input for the next iteration
        decoder_input = tf.expand_dims([predicted_index], 0)

    # Return the translated text
    return " ".join(output_text)

# Example usage
input_sentence = "How are you doing?"
translated_sentence = translate_sentence(input_sentence)

print(f"Input English Text: {input_sentence}")
print(f"Translated Marathi Text: {translated_sentence}")
'''
import tensorflow as tf

# Load the saved model
loaded_model = tf.keras.models.load_model("english_to_marathi_translation_model")

# Function for translating a sentence
def translate_sentence(input_text, source_tokenizer, target_tokenizer):
    # Explicitly convert input_text to a string
    input_text = str(input_text)

    # Tokenize and pad the input sequence
    input_seq = source_tokenizer.texts_to_sequences([input_text])
    input_seq = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=loaded_model.input[0].shape[1])

    # ... (rest of the function remains unchanged)

    # ... (rest of the function remains unchanged)

    # Initialize the decoder input with a start token
    start_token = target_tokenizer.word_index["<start>"]
    decoder_input = tf.expand_dims([start_token], 0)

    # Initialize the hidden state of the encoder with zeros
    encoder_states = [tf.zeros((1, loaded_model.input[0].shape[1])), tf.zeros((1, loaded_model.input[0].shape[1]))]

    # Initialize a list to store the Marathi translation
    output_text = []

    # Maximum length for the output sequence
    max_length = loaded_model.input[1].shape[1]

    # Perform inference
    for _ in range(max_length):
        # Predict the next word in the sequence
        predictions = loaded_model.predict([input_seq, decoder_input] + encoder_states)

        # Get the index of the predicted word
        predicted_index = tf.argmax(predictions, axis=-1).numpy()[0, 0]

        # Break if the end token is predicted
        if target_tokenizer.index_word[predicted_index] == "<end>":
            break

        # Add the predicted word to the output sequence
        output_text.append(target_tokenizer.index_word[predicted_index])

        # Update the decoder input for the next iteration
        decoder_input = tf.expand_dims([predicted_index], 0)

    # Return the translated text
    return " ".join(output_text)

# Example usage
source_texts = ["Hello, how are you?", "What is your name?", "This is a sample sentence."]
target_texts = ["नमस्कार, कसे आहात?", "तुमचं नाव काय आहे?", "ही एक नमुना वाक्य आहे."]

source_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
source_tokenizer.fit_on_texts(source_texts)

target_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
target_tokenizer.fit_on_texts(target_texts)

# Check if '<start>' token is in the target tokenizer's word index
if '<start>' not in target_tokenizer.word_index:
    # Add '<start>' token to the word index
    target_tokenizer.word_index['<start>'] = len(target_tokenizer.word_index) + 1
    target_tokenizer.index_word[target_tokenizer.word_index['<start>']] = '<start>'

    # Update the vocabulary size in the target tokenizer
    target_tokenizer.num_words = len(target_tokenizer.word_index) + 1

# Example usage with custom tokenizers
input_sentence = "How are you doing?"
translates_sentence = translate_sentence(input_sentence, source_tokenizer, target_tokenizer)

print(f"Input English Text: {input_sentence}")
print(f"Translated Marathi Text: {translates_sentence}")
