import { Inter } from "next/font/google";
import TopBar from "../components/TopBar";
import BarChart from "../components/BarChart";
import RecentOrders from "../components/RecentOrder";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
      <main className="min-h-screen bg-white">
        <TopBar />
        <div className="grid grid-cols-1 gap-4 p-4 md:grid-cols-3">
          <BarChart />
          <RecentOrders />

        </div>
      </main>
  );
}
