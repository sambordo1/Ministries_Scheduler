#ifndef WEBSOCKETCONTROLLER_H
#define WEBSOCKETCONTROLLER_H

#include <QObject>
#include <QtWebSockets/QWebSocket>

class WebSocketController : public QObject
{
    Q_OBJECT
public:
    explicit WebSocketController(QObject *parent = nullptr, QString sURL = "");

signals:
    void wsConnect();
    void wsDisconnect();
    void sendMsg(QString msg);

private:
    QString serverURL;
    QWebSocket *m_WebSocket;


private slots:
    void wsConnectSlot();
    void wsDisconnectSlot();
    qint64 wsSendMsg(QString msg);
    void wsMsgRecvd(QString msg);
    void wsStateChanged(QAbstractSocket::SocketState state);
    void wsError(QAbstractSocket::SocketError error);

};

#endif // WEBSOCKETCONTROLLER_H
