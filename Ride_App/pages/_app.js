import SideBar from "../components/SideBar.jsx";
import Header from "../components/Header.jsx";
import "../styles/globals.css";

export default function App({ Component, pageProps }) {
  return (
    <SideBar className="">
      {/* Place the Header inside the Sidebar if they are meant to be together */}
      <Header className="z-10" />
      <Component {...pageProps} />
    </SideBar>
  );
}
