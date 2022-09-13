#include "mastercontroller.h"
#include <QDebug>

MasterController::MasterController(QObject *parent,
                                   WebSocketController *wsc)
    : QObject{parent}
{
    m_wsc = wsc;
    connect(this, SIGNAL(logIn(QString,QString)), SLOT(logUserIn(QString,QString)));
}

bool MasterController::getLogIn()
{
    return loggedIn;
}

void MasterController::setLogIn(bool login)
{
    loggedIn = login;
    qDebug().nospace() << "loggedIn = " << loggedIn;
    emit logInChanged(loggedIn);
}

void MasterController::logUserIn(QString user, QString pwd)
{
    //! TODO log-in logic
    setLogIn(true);
    emit m_wsc->wsConnect();
}

void MasterController::registerUser(QString username, QString password)
{
    qDebug().nospace() << "register user (" << username << ", " << password << ")";
    emit m_wsc->sendMsg(QString("Created User: username=%1, pwd=%2").arg(username, password));
}

void MasterController::createMinistry(QString name, QString roles)
{
    qDebug().nospace() << "create ministry (" << name << ", " << roles << ")";
    emit m_wsc->sendMsg(QString("Created ministry: name=%1, roles=%2").arg(name, roles));
}
