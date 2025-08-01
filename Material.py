import streamlit as st
from pathlib import Path
import pickle
import pandas as pd
import db_handler

import data

admins = data.admins

st.title("Our Notebook (Partially)")

st.header("Here you will find the algorithm implementations for things we believe you need.")
st.subheader('''Dinic.h
Description: Flow algorithm with complexity $O(V E \\log U)$ where $U =
\\mathrm{max} |cap|$.   $O(\\mathrm{min}(E^{\\frac{1}{2}}, V^{\\frac{2}{3}})E)$ if $U = 1$;   $O(√V E)$ for bipartite matching.''')

code = """
#define sz(yarin) ((int)(yarin).size())

struct Dinic {
    struct Edge {
        int to, rev;
        ll c, oc;
        ll flow() { return max(oc - c, 0LL); } // if you need flows
    };
    vi lvl, ptr, q;
    vector<vector<Edge>> adj;
    Dinic(int n) : lvl(n), ptr(n), q(n), adj(n) {}
    void addEdge(int a, int b, ll c, ll rcap = 0) {
        adj[a].push_back({b, sz(adj[b]), c, c});
        adj[b].push_back({a, sz(adj[a]) - 1, rcap, rcap});
    }
    ll dfs(int v, int t, ll f) {
        if (v == t || !f) return f;
        for (int& i = ptr[v]; i < sz(adj[v]); i++) {
            Edge& e = adj[v][i];
            if (lvl[e.to] == lvl[v] + 1)
                if (ll p = dfs(e.to, t, min(f, e.c))) {
                    e.c -= p, adj[e.to][e.rev].c += p;
                    return p;
                }
        }
        return 0;
    }
    ll calc(int s, int t) {
        ll flow = 0; q[0] = s;
        rep(L,0,31) do { // ’ int L=30’ maybe faster for random data
                lvl = ptr = vi(sz(q));
                int qi = 0, qe = lvl[s] = 1;
                while (qi < qe && !lvl[t]) {
                    int v = q[qi++];
                    for (Edge e : adj[v])
                        if (!lvl[e.to] && e.c >> (30 - L))
                            q[qe++] = e.to, lvl[e.to] = lvl[v] + 1;
                }
                while (ll p = dfs(s, t, LLONG_MAX)) flow += p;
            } while (lvl[t]);
        return flow;
    }
    bool leftOfMinCut(int a) { return lvl[a] != 0; }
};

"""
st.code(code, language='cpp', line_numbers=True)


