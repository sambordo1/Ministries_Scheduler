import QtQuick 2.15
import QtQuick.Controls 2.15
import MinSched.Controllers 1.0
import QtQuick.Controls.Material

Item {
    anchors.fill: parent

    Button {
        id: user_button
        text: "Register User"
        anchors {
            right: parent.right
            top: parent.top
            rightMargin: 5
            topMargin: 5
        }
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
        anchors {
            right: user_button.left
            top: parent.top
            rightMargin: 5
            topMargin: 5
        }

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
                    target: popup_window
                    property: "opacity"
                    from: 0.5
                    to: 1
                    duration: 500
                }

                PropertyAnimation {
                    targets: [popup_cancel_button, popup_complete_button]
                    property: "opacity"
                    from: -1
                    to: 1
                    duration: 500
                }

                NumberAnimation {
                    target: popup_window
                    properties: "width"
                    from: 0
                    to: main_view.width * 0.75
                    easing.type: Easing.InOutQuad
                    duration: 500
                }

                NumberAnimation {
                    target: popup_window
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
                    target: popup_window
                    property: "opacity"
                    from: 1
                    to: 0.5
                    duration: 500
                }

                PropertyAnimation {
                    targets: [popup_cancel_button, popup_complete_button]
                    property: "opacity"
                    from: 1
                    to: 0
                    duration: 300
                }

                NumberAnimation {
                    target: popup_window
                    properties: "width"
                    from: main_view.width * 0.75
                    to: 0
                    easing.type: Easing.InOutQuad
                    duration: 500
                }

                NumberAnimation {
                    target: popup_window
                    properties: "height"
                    from: main_view.height * 0.75
                    to: 0
                    easing.type: Easing.InOutQuad
                    duration: 500
                }
            }
        }

        Text {
            id: popup_label1
            width: parent.width * 0.2

            anchors {
                right: popup_label2.right
                bottom: popup_label2.top
                bottomMargin: 15
            }
        }
        TextField {
            id: popup_text1
            width: parent.width * 0.7
            height: 30

            anchors {
                left: popup_label1.right
                rightMargin: 10
                verticalCenter: popup_label1.verticalCenter
            }
        }
        Text {
            id: popup_label2
            width: parent.width * 0.2

            anchors {
                left: parent.left
                leftMargin: 15
                verticalCenter: parent.verticalCenter
            }
        }
        TextField {
            id: popup_text2
            width: parent.width * 0.7
            height: 30

            anchors {
                left: popup_label2.right
                rightMargin: 10
                verticalCenter: popup_label2.verticalCenter
            }
        }
        Button {
            id: popup_cancel_button
            text: qsTr("Cancel")

            onClicked: {
                popup_window.close()
                popup_text1.text = qsTr("")
                popup_text2.text = qsTr("")
            }

            anchors {
                right: parent.horizontalCenter
                rightMargin: 10
                top: popup_label2.bottom
                topMargin: 15
            }
        }
        Button {
            id: popup_complete_button
            text: qsTr("Done")

            onClicked: {
                popup_window.close()
                if (popup_complete_button.text === qsTr("Register")) {
                    master.registerUser(popup_text1.text, popup_text2.text);
                } else if (popup_complete_button.text === qsTr("Create")) {
                    master.createMinistry(popup_text1.text, popup_text2.text);
                }

                popup_text1.text = qsTr("")
                popup_text2.text = qsTr("")
            }

            anchors {
                left: parent.horizontalCenter
                leftMargin: 10
                verticalCenter: popup_cancel_button.verticalCenter
            }
        }
    }
}
