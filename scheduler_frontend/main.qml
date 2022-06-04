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
                master.LoggedIn = true;
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
        width: 320
        height: 240
        padding: 10
        anchors.centerIn: parent
        visible: false
        modal: true
        focus: false
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

        Column {
            id: popup_column
            spacing: 10
            anchors.centerIn: parent
            Row {
                id: popup_row1
                spacing: 10
                Text {
                    id: popup_label1
                }
                TextField {
                    id: popup_text1
                    width: 240
                    height: 30
                    anchors.verticalCenter: popup_label1.verticalCenter
                }
            }
            Row {
                id: popup_row2
                spacing: 10
                Text {
                    id: popup_label2
                }
                TextField {
                    id: popup_text2
                    width: 240
                    height: 30
                    anchors.verticalCenter: popup_label2.verticalCenter
                }
            }
            Row {
                id: popup_button_row
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
                        popup_text1.text = qsTr("")
                        popup_text2.text = qsTr("")
                    }
                }
            }
        }
    }
}
