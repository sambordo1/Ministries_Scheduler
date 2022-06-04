#ifndef MASTERCONTROLLER_H
#define MASTERCONTROLLER_H

#include <QObject>

class MasterController : public QObject
{
    Q_OBJECT
    Q_PROPERTY(bool LoggedIn READ getLoggedIn WRITE setLoggedIn NOTIFY loggedInChanged)
public:
    explicit MasterController(QObject *parent = nullptr,
                              QString sURL ="");

    bool getLoggedIn();

public slots:
    void setLoggedIn(bool val);
    void registerUser(QString username, QString password);
    void createMinistry(QString name, QString roles);

signals:
    void loggedInChanged();

private:
    bool loggedIn = false;
    QString serverURL;
};

#endif // MASTERCONTROLLER_H
