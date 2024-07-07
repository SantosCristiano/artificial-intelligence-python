# pip install tensorflow opencv-python
import tensorflow as tf
import numpy as np
import cv2
import time
from absl import app, flags, logging
from absl.flags import FLAGS

# Definir as flags
flags.DEFINE_string('classes', './data/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './data/yolov3.weights', 'path to weights file')
flags.DEFINE_string('output', './output', 'path to output folder')
flags.DEFINE_string('image', './data/girl.png', 'path to input image')


# Carregar nomes de classes
def load_classes(file):
    with open(file, 'r') as f:
        class_names = f.read().splitlines()
    return class_names


# Construir o modelo YOLOv3
def build_model(num_classes):
    model = tf.keras.models.Sequential()
    # Definir a arquitetura YOLOv3 (simplificada)
    # Para simplificação, podemos carregar um modelo YOLOv3 pré-treinado usando tf.keras
    yolo = tf.keras.applications.MobileNetV2(input_shape=(416, 416, 3), include_top=False)
    model.add(yolo)
    model.add(tf.keras.layers.GlobalAveragePooling2D())
    model.add(tf.keras.layers.Dense(num_classes))
    return model


# Carregar pesos pré-treinados
def load_weights(model, weights_file):
    # Esta função deve ser personalizada para carregar os pesos YOLOv3 específicos
    model.load_weights(weights_file)


# Função para processar imagens
def process_image(img_path, model, class_names):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (416, 416))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, axis=0) / 255.0

    pred = model.predict(img)
    boxes, scores, classes, nums = tf.image.combined_non_max_suppression(
        boxes=tf.reshape(pred[:, :, :4], (tf.shape(pred)[0], -1, 1, 4)),
        scores=tf.reshape(pred[:, :, 4:], (tf.shape(pred)[0], -1, tf.shape(pred)[-1] - 4)),
        max_output_size_per_class=50,
        max_total_size=50,
        iou_threshold=0.5,
        score_threshold=0.5
    )

    return boxes, scores, classes, nums


# Função para desenhar caixas delimitadoras
def draw_boxes(img, boxes, scores, classes, nums, class_names):
    wh = np.flip(img.shape[0:2])
    for i in range(nums[0]):
        x1y1 = tuple((np.array(boxes[0][i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[0][i][2:4]) * wh).astype(np.int32))
        img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
        img = cv2.putText(img, '{} {:.2f}'.format(
            class_names[int(classes[0][i])], scores[0][i]),
                          x1y1, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
    return img


# Função principal
def main(_argv):
    class_names = load_classes(FLAGS.classes)
    model = build_model(len(class_names))
    load_weights(model, FLAGS.weights)

    img_path = FLAGS.image
    img_raw = tf.image.decode_image(open(img_path, 'rb').read(), channels=3)

    boxes, scores, classes, nums = process_image(img_path, model, class_names)
    img = cv2.cvtColor(img_raw.numpy(), cv2.COLOR_RGB2BGR)
    img = draw_boxes(img, boxes, scores, classes, nums, class_names)

    output_path = FLAGS.output + '/output.jpg'
    cv2.imwrite(output_path, img)
    print(f'Output saved to: {output_path}')


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
