import QtQuick
import QtQuick.Controls 2.15
import MinSched.Controllers 1.0

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Button {
        id: login_button
        text: master.LoggedIn ? "Logout" : "Login"
        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            color: login_button.down ? "#d6d6d6" : "#f6f6f6"
            border.color: "#26282a"
            border.width: 1
            radius: 4
        }
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: 5
        anchors.topMargin: 5
        onClicked: {
            if (master.LoggedIn) {
                master.LoggedIn = false;
            } else {
                popup_label1.text = qsTr("Username: ")
                popup_text1.placeholderText = qsTr("Enter username")
                popup_label2.text = qsTr("Password: ")
                popup_text2.placeholderText = qsTr("Enter password")
                popup_complete_button.text = qsTr("Login")
                popup_window.open()
            }
        }
    }

    Button {
        id: user_button
        text: "Register User"
        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            color: user_button.down ? "#d6d6d6" : "#f6f6f6"
            border.color: "#26282a"
            border.width: 1
            radius: 4
        }
        anchors.right: login_button.left
        anchors.top: parent.top
        anchors.rightMargin: 5
        anchors.topMargin: 5
        onClicked: {
            popup_label1.text = qsTr("Username: ")
            popup_text1.placeholderText = qsTr("Enter username")
            popup_label2.text = qsTr("Password: ")
            popup_text2.placeholderText = qsTr("Enter password")
            popup_complete_button.text = qsTr("Register")
            popup_window.open()
        }
    }

    Button {
        id: ministry_button
        text: "Create Ministry"
        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            color: ministry_button.down ? "#d6d6d6" : "#f6f6f6"
            border.color: "#26282a"
            border.width: 1
            radius: 4
        }
        anchors.right: user_button.left
        anchors.top: parent.top
        anchors.rightMargin: 5
        anchors.topMargin: 5
        onClicked: {
            popup_label1.text = qsTr("Name: ")
            popup_text1.placeholderText = qsTr("Enter ministry name")
            popup_label2.text = qsTr("Roles: ")
            popup_text2.placeholderText = qsTr("role1;role2;role3;...")
            popup_complete_button.text = qsTr("Create")
            popup_window.open()
        }
    }

    Popup {
        id: popup_window
        width: parent.width * 0.75
        height: parent.height * 0.75
        topInset: 0
        leftInset: 0
        rightInset: 0
        bottomInset: 0
        padding: 10
        anchors.centerIn: parent
        visible: false
        modal: true
        focus: false
        closePolicy: Popup.CloseOnEscape

        Column {
            id: popup_column
            width: parent.width * 0.95
            height: parent.height * 0.95
            spacing: 10
            anchors.centerIn: parent
            Row {
                id: popup_row1
                width: parent.width * 0.95
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 10
                Text {
                    id: popup_label1
                    width: parent.width * 0.2
                }
                TextField {
                    id: popup_text1
                    width: parent.width * 0.7
                    height: 30
                    anchors.verticalCenter: popup_label1.verticalCenter
                }
            }
            Row {
                id: popup_row2
                width: parent.width * 0.95
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 10
                Text {
                    id: popup_label2
                    width: parent.width * 0.2
                }
                TextField {
                    id: popup_text2
                    width: parent.width * 0.7
                    height: 30
                    anchors.verticalCenter: popup_label2.verticalCenter
                }
            }
            Row {
                id: popup_button_row
                width: parent.width * 0.95
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 10
                Button {
                    id: popup_cancel_button
                    text: qsTr("Cancel")
                    background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 40
                        color: ministry_button.down ? "#d6d6d6" : "#f6f6f6"
                        border.color: "#26282a"
                        border.width: 1
                        radius: 4
                    }
                    onClicked: {
                        popup_window.close()
                        popup_text1.text = qsTr("")
                        popup_text2.text = qsTr("")
                    }
                }
                Button {
                    id: popup_complete_button
                    text: qsTr("Done")
                    background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 40
                        color: ministry_button.down ? "#d6d6d6" : "#f6f6f6"
                        border.color: "#26282a"
                        border.width: 1
                        radius: 4
                    }
                    onClicked: {
                        popup_window.close()
                        if (popup_complete_button.text === qsTr("Register")) {
                            master.registerUser(popup_text1.text, popup_text2.text);
                        } else if (popup_complete_button.text === qsTr("Create")) {
                            master.createMinistry(popup_text1.text, popup_text2.text);
                        } else if (popup_complete_button.text === qsTr("Login")) {
                            master.LoggedIn = true;
                        }

                        popup_text1.text = qsTr("")
                        popup_text2.text = qsTr("")
                    }
                }
            }
        }
    }
}
