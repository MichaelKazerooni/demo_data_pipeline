from flask import Flask, jsonify, Response, stream_with_context
import time
import uuid
import random

app = Flask(__name__)

@app.route('/')
def main_page():
    return Response('HOMEPAGE')


@app.route('/data_generator/<int:rowcount>', methods=['GET'])
def data_generator_and_sender(rowcount):
    '''
    creates and sends dummy data
    :param rowcount:
    :return:
    doesn not return anything
    '''

    def gen_out():
        for _ in range(rowcount):
            time.sleep(0.01)
            txid = uuid.uuid4()
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000,1000), 2)
            print(f'{txid} , {uid} , {amount}')
            yield f"('{txid}','{uid}',{amount})\n"

    return Response(stream_with_context(gen_out()))



if __name__ == '__main__':
    app.run(debug = True)