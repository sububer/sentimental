import pandas as pd
import tensorflow as tf
import keras

SHUFFLE_BUFFER = 500
BATCH_SIZE = 2

df = pd.read_csv("data/train_dataset.csv")
numeric_feature_names = ['pos_mean',
                         'neg_mean',
                         'joy_mean',
                         'fear_mean',
                         'pos_std',
                         'neg_std',
                         'joy_std',
                         'fear_std']
numeric_features = df[numeric_feature_names]
target = df.pop('pct')

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
                  metrics=['mean_absolute_error'])
    return model


def get_basic_linear_regression():
    model = keras.models.Sequential([
        normalizer,
        keras.layers.Dense(1, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l1_l2(l1=0.1, l2=0.01))
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error"),
                  metrics=['mean_absolute_error'])
    return model


model = get_basic_mlp_model()
model.fit(numeric_features, target, epochs=15, batch_size=BATCH_SIZE)

model2 = get_basic_linear_regression()
model2.fit(numeric_features, target, epochs=15, batch_size=BATCH_SIZE)