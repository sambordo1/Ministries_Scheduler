#ifndef MASTERCONTROLLER_H
#define MASTERCONTROLLER_H

#include <QObject>
#include "controllers/websocketcontroller.h"

class MasterController : public QObject
{
    Q_OBJECT
    Q_PROPERTY(bool LoggedIn READ getLogIn WRITE setLogIn NOTIFY logInChanged)
public:
    explicit MasterController(QObject *parent = nullptr,
                              WebSocketController *wsc = nullptr);

    bool getLogIn();

public slots:
    void setLogIn(bool login);
    void registerUser(QString username, QString password);
    void createMinistry(QString name, QString roles);

signals:
    void logIn(QString user, QString pwd);
    void logInChanged(bool login);

private:
    bool loggedIn = false;
    WebSocketController *m_wsc;

private slots:
    void logUserIn(QString user, QString pwd);
};

#endif // MASTERCONTROLLER_H
