import { StyleSheet } from "react-native";
import { Avatar } from "react-native-paper";
export default StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      marginTop: 60,
    },
    row: {
        flexDirection:"row",
        flexWrap: "wrap"
    },
    margin:{
        margin: 5
    },
    avatar:{
        width:120,
        height:120,
        borderRadius:50
    },
    padding:{
        padding:8
    }

  });
  