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
    qDebug() << "loggedIn =" << loggedIn;
}
