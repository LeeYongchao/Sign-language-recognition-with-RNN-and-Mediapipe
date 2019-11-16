from __future__ import absolute_import, division, print_function, unicode_literals
from keras.preprocessing import sequence
from keras.datasets import imdb
from keras import layers, models
import pickle
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical


class Data:
    def __init__(self):
        
        X = []
        Y = []
        
        with open("/Users/anna/SLR/data.pkl", 'rb') as fin:
            frames = pickle.load(fin)
            for i, frame in enumerate(frames):
                features = frame[0]
                word = frame[1]
            
                X.append(np.array(features))
                Y.append(word)
        X = np.array(X)
        Y = np.array(Y)

        t = Tokenizer()
        t.fit_on_texts(Y)
        #print(t.word_index)
        #Y = to_categorical(Y,len(t.word_index))
        encoded=t.texts_to_sequences(Y)
        #print(encoded)
        one_hot=to_categorical(encoded)
        #print(one_hot)

       
        (x_train, y_train) = X, one_hot
        
        self.x_train, self.y_train = x_train, y_train
        self.x_test, self.y_test = x_train, y_train
        
        
class RNN_LSTM(models.Model):
    def __init__(self):
        x = layers.Input((8736,))
        h = layers.Embedding(8736, 128)(x)
        h = layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2)(h)
        y = layers.Dense(11, activation='softmax')(h)
        super().__init__(x, y)

        # try using different optimizers and different optimizer configs
        self.compile(loss='binary_crossentropy',
                     optimizer='adam', metrics=['accuracy'])


class Machine:
    def __init__(self):
        self.data = Data()
        self.model = RNN_LSTM()

    def run(self, epochs=3, batch_size=32):
        data = self.data
        model = self.model
        print('Training stage')
        print('==============')
        model.fit(data.x_train, data.y_train,
                  batch_size=batch_size,
                  epochs=epochs,
                  validation_data=(data.x_test, data.y_test))

        score, acc = model.evaluate(data.x_test, data.y_test,
                                    batch_size=batch_size)
        print('Test performance: accuracy={0}, loss={1}'.format(acc, score))


def main():
    m = Machine()
    m.run()


if __name__ == '__main__':
    main()
