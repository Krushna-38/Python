# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:16:37 2023

@author: Krushna Lad
"""

import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Attention
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy

# Sample data for training
source_texts = ["Hello"]
target_texts = ["नमस्कार"]

# Tokenization of source and target texts
source_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
#It has created tokenizer object to process the data
source_tokenizer.fit_on_texts(source_texts)
#Here the tokenizer will process the input text and 
#will create the vocabulary based on input text
source_seq = source_tokenizer.texts_to_sequences(source_texts)
#here all the sentences/tokens will replaced by integers
source_seq = tf.keras.preprocessing.sequence.pad_sequences(source_seq)
#It ensures that all sequences have same length
#So it will be easy during the processes of neural networks processing

target_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
#Created new tokenizer object for the targetd text 
target_tokenizer.fit_on_texts(target_texts)
#this will converts the text sequences into the integer sequences
#It will create the vocabulary of target text 
target_seq = target_tokenizer.texts_to_sequences(target_texts)
#Each word will be replaced byinteger sequence
target_seq = tf.keras.preprocessing.sequence.pad_sequences(target_seq)
#It ensures that all words have same length
# Define the model architecture
embedding_dim = 256
#It gives the dimensions of vectors
units = 512
#It represents the number of units in neural networks
#The higher units then model is more expressive

# Encoder model
encoder_inputs = Input(shape=(None,))
#Here we created input tensor for encoder.
#The 'Shape=none' explained that the input sequences have variable length
encoder_embedding = Embedding(input_dim=len(source_tokenizer.word_index) + 1, output_dim=embedding_dim)(encoder_inputs)
#It maps the input sequences and converting them into
#the fixed dimension and creating fixed dimension vector
#Then it accounts that the index starts from 1
encoder_lstm = LSTM(units, return_sequences=True, return_state=True)
#This line creates an LSTM(long short term memory) for encoder
encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding)
#This line applies the LSTM layer to the embedded sequence
#State_h contain hidden state and state_c contain cell state of LSTM at the final timestamp
encoder_states = [state_h, state_c]
#Now the list is created which containing the hidden state and cell state timestep

# Decoder model
decoder_inputs = Input(shape=(None,))
#It creates input tensor for decoder
decoder_embedding = Embedding(input_dim=len(target_tokenizer.word_index) + 1, output_dim=embedding_dim)(decoder_inputs)
#This line creates embedding layer for decoder
decoder_lstm = LSTM(units, return_sequences=True, return_state=True)
#This line creates LSTM lyer for decoder
decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
#This line applies LSTM lyers to the embedded sequences
#This connection between encoder and decoder states is key 
#Component of sequence-to-sequence model

# Attention mechanism
attention_layer = Attention(use_scale=True)
#It creates attention model for sequence-to-sequence model
attention_weights = attention_layer([decoder_outputs, encoder_outputs])
#It shows creates a attention towards the Decoder&encoders output
#It specifies that how much weight should be given to the 
#Eacch part of sequence

# Combine context vector and decoder output
decoder_combined_context = tf.concat([decoder_outputs], axis=-1)
#This line combines the information of decoder
#Axis=-1 indicates that the concatnation should start from last index

# Dense layer for prediction
decoder_dense = Dense(len(target_tokenizer.word_index) + 1, activation='softmax')
#This line creates the dense layer of decoder output
#Fully connected line
#+1 is used for accounting the unknown token
output = decoder_dense(decoder_combined_context)
#It applies the dense layer to the combined context vector obtained from the decoder.

# Create the model using the specified inputs and outputs
model = Model([encoder_inputs, decoder_inputs], output)

# Compile the model with an optimizer, loss function, and evaluation metric
model.compile(optimizer=Adam(), loss=SparseCategoricalCrossentropy(), metrics=['accuracy'])

# Train the model with the training data
model.fit([source_seq, target_seq[:, :-1]], target_seq[:, 1:], epochs=10, batch_size=64)
#Epochs=10 represents how many times model will PASS forward
#and backword during neural network training

# Save the trained model 
model.save("english_to_marathi_translation_model")
