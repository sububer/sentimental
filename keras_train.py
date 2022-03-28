import pandas as pd
import tensorflow as tf
import keras

SHUFFLE_BUFFER = 500
BATCH_SIZE = 2

df = pd.read_csv("data/2022323_infer.csv")
numeric_feature_names = ['replies', 'likes', 'tweets', 'quotes', 'pos', 'neg', 'neu', 'others', 'joy', 'sadness',
                         'anger', 'surprise', 'fear']
numeric_features = df[numeric_feature_names]
target = df.pop('btc')

tf.convert_to_tensor(numeric_features)
normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(numeric_features)


def get_basic_mlp_model():
    model = tf.keras.Sequential([
        normalizer,
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error"),
                  metrics=['accuracy'])
    return model


def get_basic_linear_regression():
    model = keras.models.Sequential([
        normalizer,
        keras.layers.Dense(1, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l1_l2(l1=0.1, l2=0.01))
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error"),
                  metrics=['accuracy'])
    return model


model = get_basic_mlp_model()
model.fit(numeric_features, target, epochs=15, batch_size=BATCH_SIZE)

model2 = get_basic_linear_regression()
model2.fit(numeric_features, taraget, epochs=15, batch_size=BATCH_SIZE)