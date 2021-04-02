

from database import db_x

msg_db = db_x["CHATBOT_MSG_DB"]


def add_msg_in_db(msg_id, sender_id, um_id):
    msg_db.insert_one({"msg_id": msg_id, "sender_id": sender_id, "um_id": um_id})


def get_user_id_frm_msg_id(msg_id):
    return msg_db.find_one({"msg_id": msg_id})
