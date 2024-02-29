import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Layer, SimpleRNN, Dense, Activation

# Define the RNN architecture


class MyRNN(Layer):
    def __init__(self, sequence_size, input_size, hidden_size, output_size, **kwargs):
        super(MyRNN, self).__init__(**kwargs)
        self.sequence_size = sequence_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.input_size = input_size

      # Create a model
        model = Sequential([
            # Dense layer for preprocessing the epitope
            SimpleRNN(hidden_size, input_shape=(
                sequence_size, input_size), return_sequences=True),
            # Assuming a binary classification task
            Dense(output_size, activation='sigmoid')
        ])

        # Compile the model
        # Example loss function, adjust as needed
        model.compile(optimizer='adam',
                      loss='binary_crossentropy', metrics=['accuracy'])
        return model

    # def build(self, input_shape):
    #     # input_shape is expected to be a tuple of two shapes: (input_shape, hidden_input_shape)
    #     input_shape, hidden_input_shape = input_shape
    #     super(MyRNN, self).build(input_shape)

    # def call(self, inputs):
    #     # inputs is a tuple of two tensors: (input_tensor, hidden_input_tensor)
    #     input_tensor, hidden_input_tensor = inputs

    #     # Hidden layer  1: Combine the tensors from input layer
    #     combined = tf.concat([input_tensor, hidden_input_tensor], axis=1)

    #     # Hidden layer  2: Linear input to output (i2o)
    #     i2o = self.i2o_layer(combined)

    #     # Hidden layer  3: Linear input to hidden output (i2h)
    #     i2h = self.i2h_layer(combined)

    #     # Hidden layer  4: Softmax on i2o
    #     output = self.softmax_layer(i2o)

    #     return output, i2h

    def init_hidden(self):
        return tf.zeros(shape=(self.hidden_size,))
