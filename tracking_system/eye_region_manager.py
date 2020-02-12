# coding:utf-8


class EyeRegionManager:
    """
    目領域を管理するクラス
    """

    def __init__(self):
        """
        初期化
        """
        self._right_eye_region = {}
        self._left_eye_region = {}
        self._right_eye_img = None
        self._left_eye_img = None
        self._right_eye_points = None
        self._left_eye_points = None

    def detect_eye_region(self, face_landmark):
        """
        ランドマークから目領域の座標を取得
        :param face_landmark:
        """
        # 右目切り出し
        self._right_eye_region = {'top_x': face_landmark[36][0], 'bottom_x': face_landmark[39][0],
                                  'top_y': face_landmark[37][1]
                                  if face_landmark[37][1] < face_landmark[38][1] else face_landmark[38][1],
                                  'bottom_y': face_landmark[41][1]
                                  if face_landmark[41][1] > face_landmark[40][1] else face_landmark[40][1]}

        # 左目切り出し
        self._left_eye_region = {'top_x': face_landmark[42][0], 'bottom_x': face_landmark[45][0],
                                 'top_y': face_landmark[43][1]
                                 if face_landmark[43][1] < face_landmark[45][1] else face_landmark[45][1],
                                 'bottom_y': face_landmark[47][1]
                                 if face_landmark[47][1] > face_landmark[46][1] else face_landmark[46][1]}

    def detect_eye_img(self, img):
        """
        目領域の座標から左右の目画像を取得
        :param img: 画像
        """
        self._right_eye_img = img[self._right_eye_region['top_y']:self._right_eye_region['bottom_y'],
                                  self._right_eye_region['top_x']:self._right_eye_region['bottom_x']]

        self._left_eye_img = img[self._left_eye_region['top_y']:self._left_eye_region['bottom_y'],
                                 self._left_eye_region['top_x']:self._left_eye_region['bottom_x']]

    def get_right_eye_region(self):
        """
        右目領域を受け渡す
        :return self._right_eye_region: 右目領域
        """
        return self._right_eye_region

    def get_left_eye_region(self):
        """
        左目領域を受け渡す
        :return self._left_eye_region: 左目領域
        """
        return self._left_eye_region

    def get_right_eye_img(self):
        """
        右目画像を受け渡す
        :return self._right_eye_img: 右目画像
        """
        return self._right_eye_img

    def get_left_eye_img(self):
        """
        左目画像を受け渡す
        :return self._left_eye_img: 左目画像
        """
        return self._left_eye_img
