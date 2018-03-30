# -*- coding:utf-8 -*-

from . import api
from flask import request, abort, current_app, jsonify, make_response
from iHome import redis_store
from iHome.utils.captcha.captcha import captcha
from iHome import constants
from iHome.utils.response_code import RET


# @api.route("/imagecode")
# def get_image_code():
#     # 1．获取传入的验证码编码，判断是否有志
#     # 2.生成图片验证码
#     # 3.保存编号和图片验证码到ｒｅｄｉｓ
#     # 4.返回验证码图片
#
#     # 1．获取传入的验证码编码，判断是否有志
#     args = request.args
#     cur = args.get("cur")
#     pre = args.get("pre")
#     print pre
#     # print cur
#     if not cur:
#         abort(403)
#
#     # 2.生成图片验证码
#     _, text, image =captcha.generate_captcha()
#     current_app.logger.debug(text)
#     # 3.保存编号和图片验证码到ｒｅｄｉｓ
#     try:
#         redis_store.delete("ImageCode_"+pre)
#         redis_store.set("ImageCode_"+cur, text, constants.IMAGE_CODE_REDIS_EXPIRES)
#     except Exception as e:
#         current_app.logger.error(e)
#         return jsonify(error=RET.DBERR, errmsg="保存验证码失败")
#
#     # 4.返回验证码图片
#     response = make_response(image)
#     response.headers["Content-Type"] = "image/jpg"
#     return response


@api.route("/imagecode")
def get_image_code():
    """
    1. 获取传入的验证码编号，并编号是否有值
    2. 生成图片验证码
    3. 保存编号 和 其对应的图片验证码内容到redis
    4. 返回验证码图片
    :return:
    """
    # current_app.logger.error("error log")
    # 1. 获取传入的验证码编号，并编号是否有值
    args = request.args
    cur = args.get("cur")
    pre = args.get("pre")
    print pre
    if not cur:
        abort(403)

    # 2. 生成图片验证码
    _, text, image = captcha.generate_captcha()
    current_app.logger.debug(text)
    # 3. 保存编号和其对应的图片验证码内容到redis
    try:
        # 删除之前保存的数据
        redis_store.delete("ImageCode_" + pre)
        # 保存到redis中的格式就是括号中的一串
        redis_store.set("ImageCode_" + cur, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        # 保存出现错误，返回JSON数据提示错误
        return jsonify(errno=RET.DBERR, errmsg="保存验证码失败")

    # 4. 返回验证码图片
    response = make_response(image)
    response.headers["Content-Type"] = "image/jpg"
    return response














