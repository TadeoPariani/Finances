import NextAuth from "next-auth";

export const { handlers, auth } = NextAuth({
  providers: [],
  callbacks: {
    async session({ session, token }) {
      return session;
    },
  },
});
