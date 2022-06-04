#include "mastercontroller.h"
#include <QDebug>

MasterController::MasterController(QObject *parent,
                                   QString sURL)
    : QObject{parent}
{
    serverURL = sURL;
}

bool MasterController::getLoggedIn()
{
    return loggedIn;
}

void MasterController::setLoggedIn(bool val)
{
    loggedIn = val;
    emit loggedInChanged();
    qDebug().nospace() << "loggedIn = " << loggedIn;
}

void MasterController::registerUser(QString username, QString password)
{
    qDebug().nospace() << "register user (" << username << ", " << password << ")";
}

void MasterController::createMinistry(QString name, QString roles)
{
    qDebug().nospace() << "create ministry (" << name << ", " << roles << ")";
}
