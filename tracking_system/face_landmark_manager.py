# coding:utf-8

import os
import dlib
from imutils import face_utils
import cv2


class FaceLandmarkManager:
    """
    顔のランドマーク管理クラス
    """

    def __init__(self):
        """
        顔のランドマーク検出ツールの呼び出し
        """
        self._face_detector = dlib.get_frontal_face_detector()
        predictor_path = 'tracking_system' + os.sep + 'shape_predictor_68_face_landmarks.dat'
        self._face_predictor = dlib.shape_predictor(predictor_path)

        # 顔のランドマークリストの初期化
        self._face_landmark_list = []

    def clear_face_landmark_list(self):
        """
        顔のランドマークリストをリセット
        """
        self._face_landmark_list = []

    def detect_face_landmark(self, img):
        """
        画像から顔のランドマークを取得し保存
        :param img: 入力画像
        """

        # 顔検出
        img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self._face_detector(img_gry, 1)

        # 検出した全顔に対して処理
        for face in faces:
            # 顔のランドマーク検出
            landmark = self._face_predictor(img_gry, face)
            # 処理高速化のためランドマーク群をNumPy配列に変換(必須)
            landmark = face_utils.shape_to_np(landmark)
            self._face_landmark_list.append(landmark)

    def draw_face_landmark_list(self, img):
        """
        顔のランドマークを画像に描画
        :param img: 描画対象の画像
        """

        # 検出した顔全てにランドマークを描画
        for landmark in self._face_landmark_list:
            for (x, y) in landmark:
                cv2.circle(img, (x, y), 1, (255, 60, 60), -1)

    def get_face_landmark_list(self):
        """
        顔のランドマークリストの受け渡し
        :return self._face_landmark_list: 顔のランドマークリスト
        """
        return self._face_landmark_list
