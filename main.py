# coding:utf-8

import argparse
import cv2
from tracking_system import FaceLandmarkManager


def get_args():
    """
    コマンドライン引数の処理
    :return args_value: 受け取ったコマンドライン引数の値
    """
    # 使用するWebカメラの番号を設定するコマンドライン引数の作成
    parser = argparse.ArgumentParser(description='Iris tracking system')
    help_msg = 'Set web-cam number.'
    parser.add_argument('CAM_NUM', default=0, nargs='?', type=int, help=help_msg)

    # コマンドライン引数の受け取り
    args = parser.parse_args()

    return args


def get_iris_from_cam(cam_no):
    """
    Webカメラから顔画像を取得し、顔から虹彩を検出する
    :param cam_no: 使用するWebカメラ番号
    """

    cap = cv2.VideoCapture(cam_no)
    face_manager = FaceLandmarkManager()

    # カメラ画像の表示('q'で終了)
    while True:
        ret, img = cap.read()

        # 顔のランドマークリストを取得
        face_manager.clear_face_landmark_list()
        face_manager.detect_face_landmark(img)

        # 顔のランドマーク描画
        face_manager.draw_face_landmark_list(img)

        # 結果の表示
        cv2.imshow('img', img)

        # 'q'が入力されるまでカメラ画像を表示し続ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 後処理
    cap.release()
    cv2.destroyAllWindows()


def main(args):
    """
    メイン関数
    :param args: コマンドライン引数の値
    :return:
    """
    # 引数で指定された番号のWebカメラを用いて虹彩跡実施
    cam_num = args.CAM_NUM
    get_iris_from_cam(cam_num)


if __name__ == '__main__':
    args_value = get_args()
    main(args_value)
