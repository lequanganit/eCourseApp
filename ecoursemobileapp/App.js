
import MyStyles from "./styles/MyStyles";
import Catogories from "./components/Categories";

import { View } from "react-native";
import Courses from "./components/Courses";
import Home from "./screens/Home/Home";

const App= ()=> {
  return (
    <View style={MyStyles.container}>
      <Home/>
    </View>
  )
}
export default App;