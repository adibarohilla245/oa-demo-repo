import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import './styles.css';

const App = () => {
    const formik = useFormik({
        initialValues: {
            name: '',
            email: '',
            password: '',
        },
        validationSchema: Yup.object({
            name: Yup.string().required('Required'),
            email: Yup.string().email('Invalid email address').required('Required'),
            password: Yup.string().required('Required'),
        }),
        onSubmit: values => {
            alert(JSON.stringify(values, null, 2));
        },
    });

    return (
        <div>
            <header>
                <h1>Welcome to My Website</h1>
                <nav>
                    <ul className="nav-bar">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#about">About</a></li>
                        <li><a href="#contact">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <p>This is a user-friendly demo website created to showcase the main text and CSS styling.</p>
                <div className="card">
                    <h2>Card Title</h2>
                    <p>This is a description of the card content. It provides additional information.</p>
                    <button className="card-button">Click Me</button>
                </div>
                <section className="signup-form">
                    <h2>Sign Up</h2>
                    <form onSubmit={formik.handleSubmit}>
                        <label htmlFor="name">Name:</label>
                        <input
                            type="text"
                            id="name"
                            name="name"
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.name}
                        />
                        {formik.touched.name && formik.errors.name ? <div>{formik.errors.name}</div> : null}
                        <label htmlFor="email">Email:</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.email}
                        />
                        {formik.touched.email && formik.errors.email ? <div>{formik.errors.email}</div> : null}
                        <label htmlFor="password">Password:</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.password}
                        />
                        {formik.touched.password && formik.errors.password ? <div>{formik.errors.password}</div> : null}
                        <button type="submit" className="submit-button">Sign Up</button>
                    </form>
                </section>
            </main>
            <footer className="footer">
                <p>&copy; 2023 Demo Website</p>
                <p>Built by Alex the AI Intern</p>
            </footer>
        </div>
    );
};

export default App;
