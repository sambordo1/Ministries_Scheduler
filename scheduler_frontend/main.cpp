#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include "controllers/mastercontroller.h"
#include "controllers/websocketcontroller.h"


int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    qmlRegisterUncreatableType<MasterController>("MinSched.Controllers", 1, 0, "MasterController",
                                                 QStringLiteral("MasterController should not be created in qml"));
    qmlRegisterUncreatableType<MasterController>("MinSched.Controllers", 1, 0, "WebSocketController",
                                                 QStringLiteral("WebSocketController should not be created in qml"));

    WebSocketController WS(nullptr, "127.0.0.1:5000");
    MasterController MC(nullptr, &WS);

    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("master", &MC);
    engine.rootContext()->setContextProperty("socket", &WS);

    const QUrl url(u"qrc:/scheduler_frontend/main.qml"_qs);
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                     &app, [url](QObject *obj, const QUrl &objUrl) {
        if (!obj && url == objUrl)
            QCoreApplication::exit(-1);
    }, Qt::QueuedConnection);
    engine.load(url);

    return app.exec();
}
