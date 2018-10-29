# -*- coding=utf-8 -*-
import sqlite3
from flask import Flask, jsonify,request


app = Flask(__name__)


@app.route('/<Size>', methods=['GET'])
def BHA_Size_filter(Size):
    # 连接数据库
    conn = sqlite3.connect('BHA.db')
    cur = conn.cursor()
    # 执行sql语句
    sql = "select CaseFile from General a inner join BHAComponent b on a.BHA_ID = b.BHA_ID where Size = '{}';".format(Size)
    # sql = "select BHA_ID from BHAComponentRow where Type = '{}';".format(Type)
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    # 关闭连接
    conn.close()
    return jsonify(
        {
            'data': result,
        })


@app.route('/<BHA_Type>', methods=['GET'])
def BHA_Type_filter(BHA_Type):
    # 连接数据库
    conn = sqlite3.connect('BHA.db')
    cur = conn.cursor()
    # 执行sql语句
    sql = "select CaseFile from General a inner join BHAComponentRow b on a.BHA_ID = b.BHA_ID where Type = '{}';".format(BHA_Type)
    # sql = "select BHA_ID from BHAComponentRow where Type = '{}';".format(Type)
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    # 关闭连接
    conn.close()
    return jsonify(
        {
            'data': result,
        })


@app.errorhandler(404)
def page_not_found(e):
    res = jsonify({'error': 'not found'})
    res.status_code = 404
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


