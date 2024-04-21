import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "UI/UX Research Study",
    description: "User data is anonymous and strictly limited to interaction with the website."};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="safe-top">
          {children}
        </div>
      </body>
    </html>
  );
}
