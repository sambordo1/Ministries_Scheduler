import QtQuick
import QtQuick.Controls 2.15
import MinSched.Controllers 1.0

Window {
    id: main_window
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Rectangle {
        id: top_bar
        height: 55
        width: 0.95 * parent.width
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.top: parent.top
        color: "#111111"
        border {
            color: "#000000"
            width: 2
        }

        Button {
            id: menu_button
            anchors {
                left: parent.left
                verticalCenter: parent.verticalCenter
                leftMargin: 5
            }

            text: "Menu"

            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 40
                color: parent.down ? "#303030" : "#3f3f3f"
                border.color: "#26282a"
                border.width: 1
                radius: 4
            }

            contentItem: Text {
                text: parent.text
                font: parent.font
                opacity: enabled ? 1.0 : 0.3
                color: parent.down ? "#a0a0a0" : "#f0f0f0"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            onClicked: {
                if (master.LoggedIn) {
                    master.LoggedIn = false;
                } else {
                    menu_popup.open()
                }
            }
        }

        Button {
            id: login_button
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            anchors.rightMargin: 5

            text: master.LoggedIn ? "Logout" : "Login"

            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 40
                color: parent.down ? "#303030" : "#3f3f3f"
                border.color: "#26282a"
                border.width: 1
                radius: 4
            }
            contentItem: Text {
                text: login_button.text
                font: login_button.font
                opacity: enabled ? 1.0 : 0.3
                color: login_button.down ? "#a0a0a0" : "#f0f0f0"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            onClicked: {
                if (master.LoggedIn) {
                    master.LoggedIn = false;
                    socket.wsDisconnect();
                } else {
                    login_popup.open()
                }
            }
        }
    }

    Rectangle {
        id: main_view
        height: parent.height - top_bar.height
        width: 0.95 * parent.width
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.top: top_bar.bottom
        color: "#222222"
        border {
            color: "#000000"
            width: 2
        }

        Loader {
            id: main_loader
            source: "views/management.qml"
            anchors.fill: parent
        }
    }

    Popup {
        id: menu_popup
        width: 0
        height: parent.height

        x: 0
        y: 0

        visible: false
        modal: true
        focus: false
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

        background: Rectangle {
            anchors.fill: parent
            color: "#181818"
            radius: 4
        }

        enter: Transition {
            ParallelAnimation {

                PropertyAnimation {
                    target: menu_popup
                    property: "opacity"
                    from: 0.5
                    to: 1
                    duration: 500
                }

                NumberAnimation {
                    target: menu_popup
                    properties: "width"
                    from: 0
                    to: main_view.width * 0.4
                    easing.type: Easing.InOutQuad
                    duration: 500
                }
            }
        }

        exit: Transition {
            ParallelAnimation {

                PropertyAnimation {
                    target: menu_popup
                    property: "opacity"
                    from: 1
                    to: 0.5
                    duration: 500
                }

                NumberAnimation {
                    target: menu_popup
                    properties: "width"
                    from: main_view.width * 0.4
                    to: 0
                    easing.type: Easing.InOutQuad
                    duration: 500
                }
            }
        }
    }

    Popup {
        id: login_popup
        topInset: 0
        leftInset: 0
        rightInset: 0
        bottomInset: 0
        padding: 10
        anchors.centerIn: parent
        visible: false
        modal: true
        focus: false
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

        enter: Transition {

            ParallelAnimation {

                PropertyAnimation {
                    target: login_popup
                    property: "opacity"
                    from: 0.5
                    to: 1
                    duration: 500
                }

                PropertyAnimation {
                    targets: [login_cancel_button, login_complete_button]
                    property: "opacity"
                    from: -1
                    to: 1
                    duration: 500
                }

                NumberAnimation {
                    target: login_popup
                    properties: "width"
                    from: 0
                    to: main_view.width * 0.75
                    easing.type: Easing.InOutQuad
                    duration: 500
                }

                NumberAnimation {
                    target: login_popup
                    properties: "height"
                    from: 0
                    to: main_view.height * 0.75
                    easing.type: Easing.InOutQuad
                    duration: 500
                }
            }
        }

        exit: Transition {

            ParallelAnimation {

                PropertyAnimation {
                    target: login_popup
                    property: "opacity"
                    from: 1
                    to: 0.5
                    duration: 500
                }

                PropertyAnimation {
                    targets: [login_cancel_button, login_complete_button]
                    property: "opacity"
                    from: 1
                    to: 0
                    duration: 300
                }

                NumberAnimation {
                    target: login_popup
                    properties: "width"
                    from: main_view.width * 0.75
                    to: 0
                    easing.type: Easing.InOutQuad
                    duration: 500
                }

                NumberAnimation {
                    target: login_popup
                    properties: "height"
                    from: main_view.height * 0.75
                    to: 0
                    easing.type: Easing.InOutQuad
                    duration: 500
                }
            }
        }

        Text {
            id: user_label
            width: parent.width * 0.2
            text: qsTr("Username: ")

            anchors {
                right: pwd_label.right
                bottom: pwd_label.top
                bottomMargin: 15
            }
        }
        TextField {
            id: user_text
            width: parent.width * 0.7
            height: 30
            placeholderText: qsTr("Enter username")

            anchors {
                left: user_label.right
                rightMargin: 10
                verticalCenter: user_label.verticalCenter
            }
        }
        Text {
            id: pwd_label
            width: parent.width * 0.2
            text: qsTr("Password: ")

            anchors {
                left: parent.left
                leftMargin: 15
                verticalCenter: parent.verticalCenter
            }
        }
        TextField {
            id: pwd_text
            width: parent.width * 0.7
            height: 30
            placeholderText: qsTr("Enter password")

            anchors {
                left: pwd_label.right
                rightMargin: 10
                verticalCenter: pwd_label.verticalCenter
            }
        }
        Button {
            id: login_cancel_button
            text: qsTr("Cancel")

            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 40
                color: login_cancel_button.down ? "#d6d6d6" : "#f6f6f6"
                border.color: "#26282a"
                border.width: 1
                radius: 4
            }

            onClicked: {
                login_popup.close()
                user_text.text = qsTr("")
                pwd_text.text = qsTr("")
            }

            anchors {
                right: parent.horizontalCenter
                rightMargin: 10
                top: pwd_label.bottom
                topMargin: 15
            }
        }
        Button {
            id: login_complete_button
            text: qsTr("Login")

            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 40
                color: login_complete_button.down ? "#d6d6d6" : "#f6f6f6"
                border.color: "#26282a"
                border.width: 1
                radius: 4
            }

            onClicked: {
                login_popup.close()
                master.logIn(user_text.text, pwd_text.text)

                user_text.text = qsTr("")
                pwd_text.text = qsTr("")
            }

            anchors {
                left: parent.horizontalCenter
                leftMargin: 10
                verticalCenter: login_cancel_button.verticalCenter
            }
        }
    }
}
