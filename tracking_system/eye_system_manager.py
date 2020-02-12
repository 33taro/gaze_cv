# coding:utf-8

import cv2

from tracking_system import EyeRegionManager
from utility import p_tile_threshold

# Pタイル法用：眼球画像における虹彩の割合
IRIS_PER = 0.4


class EyeSystemManager:
    """
    目関連の処理の管理クラス
    """

    def __init__(self):
        # 目のランドマークの初期化
        self._eye_info = None

    def detect_eye_region(self, face_landmark):
        """
        顔のランドマークから目の領域を取得
        :param face_landmark:
        """
        # 顔のランドマークから両目の領域を格納後、リストへ追加
        eye_info = EyeRegionManager()
        eye_info.detect_eye_region(face_landmark)

        self._eye_info = eye_info

    @staticmethod
    def _detect_iris(eye_img):
        # グレースケール化後、ガウシアンフィルタによる平滑化
        eye_img_gry = cv2.cvtColor(eye_img, cv2.COLOR_BGR2GRAY)
        eye_img_gau = cv2.GaussianBlur(eye_img_gry, (5, 5), 0)

        # Pタイル法による2値化
        eye_img_thr = p_tile_threshold(eye_img_gau, IRIS_PER)

        cv2.rectangle(eye_img_thr, (0, 0), (eye_img_thr.shape[1] - 1, eye_img_thr.shape[0] - 1), (255, 255, 255), 1)

        # 輪郭抽出
        contours, hierarchy = cv2.findContours(eye_img_thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 輪郭から最小外接円により虹彩を求める
        iris = {'center': (0, 0), 'radius': 0}
        for i, cnt in enumerate(contours):
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)

            # 半径が大きすぎる場合、虹彩候補から除外
            if eye_img_thr.shape[0] < radius*0.8:
                # # 虹彩候補の描画
                # cv2.circle(eye_img, center, radius, (255, 0, 0))
                continue

            # 最も半径が大きい円を虹彩と認定
            if iris['radius'] < radius:
                iris['center'] = center
                iris['radius'] = radius
                iris['num'] = i

        return iris

    def detect_iris_info(self, img):
        """
        両目の虹彩の取得
        :param img:
        :return:
        """

        # 眼球画像の取得
        self._eye_info.detect_eye_img(img)
        right_eye_img = self._eye_info.get_right_eye_img()
        left_eye_img = self._eye_info.get_left_eye_img()

        # 眼球画像から虹彩を抽出
        right_iris = self._detect_iris(right_eye_img)
        left_iris = self._detect_iris(left_eye_img)

        # 元画像における眼球座標と、眼球画像からの相対的な虹彩座標から、
        # 元画像における虹彩座標を計算
        right_eye_region = self._eye_info.get_right_eye_region()
        left_eye_region = self._eye_info.get_left_eye_region()

        right_center = (int(right_iris['center'][0] + right_eye_region['top_x']),
                        int(right_iris['center'][1] + right_eye_region['top_y']))
        left_center = (int(left_iris['center'][0] + left_eye_region['top_x']),
                       int(left_iris['center'][1] + left_eye_region['top_y']))

        right_iris['center'] = right_center
        left_iris['center'] = left_center

        return right_iris, left_iris

    def get_eye_region(self):
        """
        目領域の受け渡し
        :return self._eye_region: 目領域
        """
        return self._eye_info
