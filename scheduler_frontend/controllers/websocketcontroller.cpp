#include "websocketcontroller.h"
#include <QDebug>

WebSocketController::WebSocketController(QObject *parent, QString sURL)
    : QObject{parent}
{
    serverURL = sURL;
    m_WebSocket = new QWebSocket(QString(), QWebSocketProtocol::VersionLatest, this);

    connect(this, SIGNAL(wsConnect()), SLOT(wsConnectSlot()));
    connect(this, SIGNAL(wsDisconnect()), SLOT(wsDisconnectSlot()));
    connect(this, SIGNAL(sendMsg(QString)), SLOT(wsSendMsg(QString)));
}

void WebSocketController::wsConnectSlot()
{
    qDebug().nospace() << "WebSocket opening: " << QString("ws://%1/ws").arg(serverURL);
    QUrl url = QUrl(QString("ws://%1/ws").arg(serverURL));
    m_WebSocket->open(url);
    connect(m_WebSocket, SIGNAL(textMessageReceived(QString)), this, SLOT(wsMsgRecvd(QString)));
    connect(m_WebSocket, SIGNAL(stateChanged(QAbstractSocket::SocketState)), this, SLOT(wsStateChanged(QAbstractSocket::SocketState)));
    connect(m_WebSocket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(wsError(QAbstractSocket::SocketError)));
}

void WebSocketController::wsDisconnectSlot()
{
    m_WebSocket->close();
}

qint64 WebSocketController::wsSendMsg(QString msg)
{
    return m_WebSocket->sendTextMessage(msg);
}

void WebSocketController::wsMsgRecvd(QString msg)
{
    qDebug().nospace() << "WebSocket message reecived: " << msg;
}

void WebSocketController::wsStateChanged(QAbstractSocket::SocketState state)
{
    switch (state) {
    case QAbstractSocket::SocketState::ConnectingState:
        qDebug().nospace() << "WebSocket connecting...";
        break;
    case QAbstractSocket::SocketState::ConnectedState:
        qDebug().nospace() << "WebSocket connected";
        break;
    case QAbstractSocket::SocketState::ClosingState:
        qDebug().nospace() << "WebSocket closing...";
        break;
    case QAbstractSocket::SocketState::UnconnectedState:
        qDebug().nospace() << "WebSocket disconnected";
        //! TODO close connections
        break;
    default:
        break;
    }
}

void WebSocketController::wsError(QAbstractSocket::SocketError error)
{
    qDebug().nospace() << "WebSocket message reecived: " << error;
}
