import streamlit as st

st.set_page_config(layout="wide")

if 'kontrol' not in st.session_state:
    st.session_state['kontrol']={'kover':True, 'pertemuan1':False, 'pertemuan2':False, 'pertemuan3':False}

class tulisan:
    def __init__(self, tulis, ukuran):
        self.tulis = tulis
        self.ukuran = ukuran
    def tampilkan(self):
        st.components.v1.html(self.tulis,height=self.ukuran)

#===============================

def pendahuluan():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/pengelolaanPendidikan/kover.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan1():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/pengelolaanPendidikan/Bab1.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan2():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/pengelolaanPendidikan/Bab2.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()
    
def Pertemuan3():
    menu1 = st.tabs(['Materi','Tugas'])
    with menu1[0]:
        tulisanHTML='<iframe src="https://martin-bernard26.github.io/pengelolaanPendidikan/pertemuan3.html" width=100% height=1000px></iframe>'
        tampil = tulisan(tulisanHTML,1000)
        tampil.tampilkan()
    with menu1[1]:
        pass
#================================

if st.session_state['kontrol']['kover']:
    pendahuluan()
if st.session_state['kontrol']['pertemuan1']:
    Pertemuan1()
if st.session_state['kontrol']['pertemuan2']:
    Pertemuan2()
if st.session_state['kontrol']['pertemuan3']:
    Pertemuan3()


#===============================

if st.sidebar.button("Pendahuluan"):
    st.session_state['kontrol']={'kover':True, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False}
    st.rerun()

if st.sidebar.button("Bab 1"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':True, 'pertemuan2':False,
                                 'pertemuan3':False}
    st.rerun()

if st.sidebar.button("Bab 2"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':True,
                                 'pertemuan3':False}
    st.rerun()

if st.sidebar.button("Bab 3"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':True}
    st.rerun()
