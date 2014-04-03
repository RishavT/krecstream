import QtQuick 2.0
import org.kde.plasma.core 2.0 as PlasmaCore
import lol 1.0
// import "plasmapackage:mod/x.py" as Lol
// Item {
//     Grid {
//         columns: 2
//         spacing: 30
//         Text{ id: one ; text: "jjaja"}
//         Text{text: "jojo"}
//         Text{text: "lala"}
//         Rectangle {
//             id: button
//             
//             color: "grey"
//             width: 150; height: 75
// 
//             Text{
//                 id: buttonLabel
//                 anchors.centerIn: parent
//                 text: "button label"
//             }
//             property color buttonColor: "lightblue"
//             property color onHoverColor: "gold"
//             property color borderColor: "white"
// 
//             signal buttonClick()
//             onbuttonClick:
//             {
//                 one.text="clicked!";
//             }
// 
//             MouseArea{
//                 anchors.fill: parent
//                 onClicked: print "lol"
//                 hoverEnabled: true
//                 
//                 onEntered: parent.color = onHoverColor
//                 onExited:  parent.color = borderColor
//             }
// 
//             //determines the color of the button by using the conditional operator
// //             color: buttonMouseArea.pressed ? Qt.darker(buttonColor, 1.5) : buttonColor
//         }
//     }
// }

// Item {
//     width: 200
//     height: 300
//     Text { text:"lol"}
// }
//     Text {
//         id: first
//         text: i18n("1st line")
//         anchors { 
//             top: parent.top;
//             left: parent.left;
//             right: parent.right;
//         }
//     }
//     Text {
//         id: second
//         text: i18n("2nd line")
//         anchors {
//             top: first.bottom;
//             left: parent.left;
//             right: parent.right;
//             bottom: parent.bottom;
//         }
//     }
    Lol.Person {
        name : "lol"
        showsize : 12
    }
